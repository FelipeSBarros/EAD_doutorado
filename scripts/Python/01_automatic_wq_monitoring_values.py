import logging
from glob import glob
from pathlib import Path
from re import sub

import pandas as pd

logging.basicConfig(level=logging.INFO)

FINAL_PATH = Path(
    "./datos/mediciones/OAN_tiempo_real/Automatic_WQ_monitoring_stations.csv"
)

stations_coords = {
    ("Blanvira", "Boya_Blanvira"): (-32.840556, -56.570278),
    ("Blanvira", "Rincon_del_Bonete"): (-32.829722, -56.418889),
    ("Blanvira", "Baygorria"): (-32.879167, -56.802500),
}


def setup_names(excel_file):
    logging.info(f"Organizing names...")
    source = f"{excel_file.split()[1]}"
    station_name = f"{sub(' ', '_', excel_file.split('_')[3])}"
    return source, station_name


logging.info("Starting script to organize automatic WQ monitoring values...")
if not FINAL_PATH.exists():
    logging.info("Concatenating data from all automatic WQ monitoring satations...")
    xlsx_list = glob("./datos/mediciones/OAN_tiempo_real/Descarga*.xlsx")
    final_df = pd.DataFrame()
    for excel_file in xlsx_list:
        # excel_file = xlsx_list[-3]

        source, station_name = setup_names(excel_file)

        logging.info(f"Reading {excel_file}...")
        df = pd.read_excel(excel_file)
        df["Station"] = station_name
        df["Source"] = source

        logging.info(f"Concatenating DataFrames...")
        final_df = pd.concat([df, final_df])

    logging.info("Adding coordinates...")
    final_df[["lat", "lon"]] = final_df.apply(
        lambda row: pd.Series(
            stations_coords.get((row["Source"], row["Station"]), (None, None))
        ),
        axis=1,
    )

    final_df.to_csv(FINAL_PATH, index=False)
    logging.info(f"Final CSV saved in {FINAL_PATH}")
