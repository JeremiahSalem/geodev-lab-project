import geopandas as gpd
import pandas as pd
from pathlib import Path

Path("data/processed").mkdir(parents=True, exist_ok=True)

TARGET_CRS = "EPSG:32631"

files = {
    "settlements": "data/processed/settlement_extent_UTM31.gpkg",
    "waste_points": "data/processed/Waste_collection_point_UTM31.gpkg",
    "city_boundary": "data/processed/Benin_city_UTM31.gpkg",
    "roads": "data/processed/RMinor_roads_BeninUTM31.gpkg",
}


def null_report(gdf, name, top=15):
    nulls = gdf.drop(columns="geometry").isna().sum()
    report = pd.DataFrame({
        "nulls": nulls,
        "pct_null": (nulls / len(gdf) * 100).round(1),
    })
    report = report[report["nulls"] > 0].sort_values("pct_null", ascending=False)
    print(f"{name}: {len(report)} of {gdf.shape[1] - 1} columns have nulls")
    print(report.head(top).to_string())
    print("empty geometries:", gdf.geometry.is_empty.sum())


layers = {}
for name, path in files.items():
    print("=" * 50)
    print(name, "->", path)
    gdf = gpd.read_file(path)
    gdf.columns = gdf.columns.str.strip()  # removes the hidden newline in pct_uncovered
    print("rows and columns:", gdf.shape)
    print("CRS:", gdf.crs)
    null_report(gdf, name)
    layers[name] = gdf

# fill rate of the road tags you are most likely to use
roads = layers["roads"]
for col in ["highway", "name", "surface", "lanes"]:
    if col in roads.columns:
        print(f"roads.{col}: {roads[col].notna().mean() * 100:.1f}% filled")
        
def drop_mostly_empty(gdf, threshold=0.99, keep=()):
    empty = [c for c in gdf.columns
             if c != "geometry" and c not in keep and gdf[c].isna().mean() > threshold]
    print("dropping", len(empty), "mostly empty columns")
    return gdf.drop(columns=empty)

for key, keep in {"roads": ("highway", "name", "surface", "lanes"), "waste_points": ()}.items():
    layers[key] = drop_mostly_empty(layers[key], keep=keep)

# ---- Step 1: pick the three urban LGAs ----
print("=" * 50)
lga = gpd.read_file("data/raw/Edo_state_LGAs.shp")
print("LGA columns:", lga.columns.tolist())


def find_name_column(gdf, target="OREDO"):
    for col in gdf.columns:
        if col == "geometry":
            continue
        values = gdf[col].astype("string").str.upper()
        if values.str.contains(target, na=False).any():
            return col
    return None


name_col = find_name_column(lga)
if name_col is None:
    raise SystemExit("No column contains 'Oredo'. Check the LGA columns printed above.")

clean = (
    lga[name_col].astype("string").str.upper()
    .str.replace(r"[-'’]", " ", regex=True)
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
)
urban = lga[clean.str.contains("OREDO|EGOR|IKPOBA", na=False)].copy()
print("urban LGAs found:", urban[name_col].tolist())
if len(urban) != 3:
    print("WARNING: expected 3 LGAs (Oredo, Egor, Ikpoba-Okha). Check the names above.")

urban = urban.to_crs(TARGET_CRS)
study_area = urban.dissolve()
study_area.to_file("data/processed/study_area_urban_UTM31.gpkg", layer="study_area", driver="GPKG")
print("study area bounds:", study_area.total_bounds)

# ---- Step 2: clip each layer to the study area ----
clip_jobs = {
    "settlements": "settlement_extent_urban_UTM31",
    "waste_points": "Waste_collection_point_urban_UTM31",
    "roads": "roads_urban_UTM31",
}
for key, out_name in clip_jobs.items():
    before = len(layers[key])
    clipped = gpd.clip(layers[key], study_area)
    clipped.to_file(f"data/processed/{out_name}.gpkg", layer=out_name, driver="GPKG")
    print(f"{key}: {before} -> {len(clipped)} features, saved {out_name}.gpkg")






# import geopandas as gpd

# files = {
#     "settlements": "data/processed/settlement_extent_UTM31.gpkg",
#     "waste_points": "data/processed/Waste_collection_point_UTM31.gpkg",
#     "city_boundary": "data/processed/Benin_city_UTM31.gpkg",
#     "roads": "data/processed/RMinor_roads_BeninUTM31.gpkg",
# }

# for name, path in files.items():
#     print("=" * 50)
#     print(name, "->", path)
#     print("layers in file:", gpd.list_layers(path)["name"].tolist())

#     gdf = gpd.read_file(path)
#     gdf = gpd.read_file("data/processed/settlement_extent_UTM31.gpkg")
#     gdf.columns = gdf.columns.str.strip()

#     print(gdf.head())
#     print("rows and columns:", gdf.shape)
#     print(gdf.geom_type.value_counts())
#     print("CRS:", gdf.crs)
#     print("Bounds:", gdf.total_bounds)