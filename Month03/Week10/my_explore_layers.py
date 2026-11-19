import geopandas as gpd
from pathlib import Path

layers = {
    "study_area": ("data/processed/study_area_urban_UTM31.gpkg", "study_area"),
    "settlements": ("data/processed/settlement_extent_urban_UTM31.gpkg", "settlement_extent_urban_UTM31"),
    "waste_points": ("data/processed/Waste_collection_point_urban_UTM31.gpkg", "Waste_collection_point_urban_UTM31"),
    "roads": ("data/processed/roads_urban_UTM31.gpkg", "roads_urban_UTM31"),
    "settlements_recalc": ("data/processed/settlement_extent_urban_recalc_UTM31.gpkg", "settlement_extent_urban_recalc"),
}

for name, (path, layer) in layers.items():
    print("=" * 50)
    print(name, "->", path)

    if not Path(path).exists():
        print("file not found, skipping (run the script that creates it first)")
        continue

    gdf = gpd.read_file(path, layer=layer)
    gdf.columns = gdf.columns.str.strip()

    print(gdf.head())
    print("rows and columns:", gdf.shape)
    print(gdf.geom_type.value_counts())
    print("CRS:", gdf.crs)
    print("Bounds:", gdf.total_bounds)
    
    roads = gpd.read_file("data/processed/roads_urban_UTM31.gpkg")
print("no highway tag:", roads["highway"].isna().sum())
print(roads["highway"].value_counts(dropna=False).head(10))