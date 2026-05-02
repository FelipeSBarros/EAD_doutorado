from pystac_client import Client
import pandas as pd
from pathlib import Path
import logging
from glob import glob
import mgrs
from datetime import datetime

C_ID = "sh-2e2a6c26-33d0-4e20-8fba-de4976e3ec2a"
C_SECRET = "kisalVftem7UKEQMv3FkPdoNANTb1C4d"

logging.info("Starting matchup process")

automatic_stations_csv = glob("./datos/mediciones/OAN_tiempo_real/*.csv")
as_df = pd.read_csv(automatic_stations_csv[0])
as_df["Fecha del dato"] = pd.to_datetime(as_df["Fecha del dato"])
as_df["date"] = as_df["Fecha del dato"].dt.date

unique_records = as_df.drop_duplicates(subset=["lat", "lon", "date"]).copy()

m = mgrs.MGRS()
unique_records["tile_mgrs"] = unique_records.apply(
    lambda row: m.toMGRS(row["lat"], row["lon"])[:5],  # primeros 5 chars = tile
    axis=1,
)
unique_records = unique_records[["lat", "lon", "date", "tile_mgrs"]].reset_index(
    drop=True
)
logging.info("Adding tile info to DataFrame")
dates_lookup = unique_records.drop_duplicates(subset=["date", "tile_mgrs"])

colecao = "sentinel-2-l1c"
max_cloud = 10

# Pasta para salvar CSV
pastadestino = Path("./datos/")
if not pastadestino.exists():
    print(f"Diretório {pastadestino} não existe. Criando...")
    pastadestino.mkdir(parents=True, exist_ok=True)

# Conectar ao catálogo AWS Earth Search
providers = {
    # "Planetary Computer": "https://planetarycomputer.microsoft.com/api/stac/v1",
    # "Earth Search (Element84)": "https://earth-search.aws.element84.com/v1", # Not .SAFE
    # "Google Earth Engine": "https://earthengine.openeo.org/v1.0/",
    # "ESA": "https://eocat.esa.int/eo-catalogue/",
    # "INPE": "https://data.inpe.br/bdc/stac/v1/",
    # "Sentinel Hub": "https://services.sentinel-hub.com/api/v1/catalog/1.0.0/",
    "DataSpace": "https://stac.dataspace.copernicus.eu/v1",
}

# Lista para armazenar metadados
from collections import defaultdict

results = defaultdict(lambda: defaultdict(list))

for _, row in dates_lookup.iterrows():
    search_date = row.date.strftime("%Y-%m-%d")

    for provider_name, provider_url in providers.items():
        print(f"\nTrying {provider_name} for {search_date}...")

        catalog = Client.open(provider_url)

        search = catalog.search(
            collections=colecao,
            datetime=search_date,
            intersects={"type": "Point", "coordinates": (row.lon, row.lat)},
            query={"eo:cloud_cover": {"lt": max_cloud}},
        )

        items = list(search.get_items())

        if not items:
            print(f"No items found for {provider_name} on {search_date}")
            continue

        for item in items:
            results[row.tile_mgrs][item.datetime.date()].append(item.id)

df = pd.DataFrame(results)
df.to_csv(pastadestino / "matchup_sentinel2_tiles.csv", index=False)


import requests

client_id = C_ID
client_secret = C_SECRET
token_url = "https://services.dataspace.copernicus.eu/auth/realms/sh/protocol/openid-connect/token"

data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
}

resp = requests.post(token_url, data=data)
resp.raise_for_status()
token = resp.json()
access_token = token["access_token"]

print("Token obtido:", access_token[:20], "...")  # só para conferir
