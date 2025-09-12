from pystac_client import Client
import rasterio
from pyproj import Transformer
import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path
import os
import logging
from glob import glob
import mgrs
from planetary_computer import sign_url

# from stackstac.download import download_item

logging.info("Starting matchup process")

automatic_stations_csv = glob("./datos/mediciones/OAN_tiempo_real/*.csv")
as_df = pd.read_csv(automatic_stations_csv[0])
as_df["Fecha del dato"] = pd.to_datetime(as_df["Fecha del dato"])
as_df["date"] = as_df["Fecha del dato"].dt.date

unique_records = as_df.drop_duplicates(subset=["lat", "lon"]).copy()

m = mgrs.MGRS()
unique_records["tile_mgrs"] = unique_records.apply(
    lambda row: m.toMGRS(row["lat"], row["lon"])[:5],  # primeros 5 chars = tile
    axis=1,
)
unique_records = unique_records[["lat", "lon", "tile_mgrs"]].reset_index(drop=True)
logging.info("Adding tile info to DataFrame")
as_df = as_df.merge(unique_records, on=["lat", "lon"], how="left")

dates_lookup = as_df.drop_duplicates(subset=["tile_mgrs", "date"])

colecao = "sentinel-2-l2a"
max_cloud = 10
level = "Level-2A"


# Pasta para salvar CSV
pastadestino = Path("datos/l")
if not pastadestino.exists():
    print(f"Diretório {pastadestino} não existe. Criando...")
    pastadestino.mkdir(parents=True, exist_ok=True)

# Parâmetro opcional: ID específico
asset_id_param = None  # ex.: "S2B_23LKP_20240607_0_L2A"

# Conectar ao catálogo AWS Earth Search
providers = {
    "Planetary Computer": "https://planetarycomputer.microsoft.com/api/stac/v1",
    # "Earth Search (Element84)": "https://earth-search.aws.element84.com/v1",
    # "Astraea": "https://stac.astraea.earth/",
    # "Google Earth Engine": "https://earthengine-stac.googleapis.com/v1"
}


# Lista para armazenar metadados
results = {}
for date in dates_lookup[:3]:
    # date = dates_lookup.iloc[10]
    for provider_name, provider_url in providers.items():
        try:
            print(f"\nTrying {provider_name}...")
            catalog = Client.open(provider_url)
            search = catalog.search(
                collections=colecao,
                # datetime="2023-01-15",#item.date.strftime("%Y-%m-%d"),
                datetime="2023-01-15/2023-01-16",
                query={
                    # "eo:cloud_cover": {"lt": 50},
                    "s2:mgrs_tile": {"eq": "21HWD"},  # item["tile_mgrs"]},
                    # "s2:processing_level": {"eq": level}  # nível de processamento
                },
                max_items=5,
            )
            items = list(search.get_items())
            results[provider_name] = {
                "count": len(items),
                "items": [item.id for item in items],
                "url": provider_url,
            }

            print(f"   ✅ Encontrados: {len(items)} itens")
            for item in items:
                print(f"      • {item.id} | {item.datetime}")

        except Exception as e:
            print(f"   ❌ Erro em {provider_name}: {e}")
            results[provider_name] = {"error": str(e)}
