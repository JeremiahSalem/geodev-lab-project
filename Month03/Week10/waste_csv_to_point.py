import pandas as pd
import geopandas as gpd
from pathlib import Path

table = pd.read_csv("data/raw/waste_collection_points.csv")
print(table.head(3))

waste_points = gpd.GeoDataFrame(
    table,
    geometry=gpd.points_from_xy(table["longitude"], table["latitude"]),
    crs="EPSG:4326"
)
print(waste_points.head(3))
print(waste_points.crs)

Path("data/processed").mkdir(parents=True, exist_ok=True)
waste_points.to_file("data/processed/waste_points.gpkg", layer="waste_points", driver="GPKG")
print("saved", len(waste_points), "waste points")