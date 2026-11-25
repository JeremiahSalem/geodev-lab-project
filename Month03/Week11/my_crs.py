import geopandas as gpd

lga = gpd.read_file("data/raw/Edo_state_LGAs.shp")
print("CRS", lga.crs)

print("suggested UTM:", lga.estimate_utm_crs())

lga_utm = lga.to_crs(epsg=32631)
lga_utm["area_wrong"] = lga.to_crs(epsg=4326).area   # area in degrees: the wrong way
lga_utm["area_km2"] = lga_utm.area / 1000000          # area in metres, converted to km2
print(lga_utm[["lganame", "area_wrong", "area_km2"]].head(3))
print("Edo State total:", round(lga_utm["area_km2"].sum(), 1), "km2")

urban = lga_utm[lga_utm["lganame"].isin(["Oredo", "Egor", "Ikpoba-Okha"])]
print(urban[["lganame", "area_km2"]])
print("Benin City urban LGAs total:", round(urban["area_km2"].sum(), 1), "km2")

study = gpd.read_file("data/processed/study_area_urban_UTM31.gpkg")
print("study area file:", round(study.area.sum() / 1000000, 1), "km2")

from pathlib import Path

# ---------- CRS of every layer ----------
layers = {
    "LGAs (raw)": "data/raw/Edo_state_LGAs.shp",
    "waste points (raw)": "data/raw/Waste_collection_Points_Benin_City.shp",
    "settlements (processed)": "data/processed/settlement_extent_urban_UTM31.gpkg",
    "roads (processed)": "data/processed/roads_urban_UTM31.gpkg",
    "waste points (processed)": "data/processed/Waste_collection_point_urban_UTM31.gpkg",
    "study area (processed)": "data/processed/study_area_urban_UTM31.gpkg",
}
for name, path in layers.items():
    if not Path(path).exists():
        print(name, "-> file not found, skipped")
        continue
    g = gpd.read_file(path)
    print(f"{name}: CRS {g.crs.to_string()} | suggested UTM {g.estimate_utm_crs().to_string()}")

# ---------- length for the line layer ----------
roads = gpd.read_file("data/processed/roads_urban_UTM31.gpkg").to_crs(epsg=32631)
roads = roads[roads["highway"].notna()]
print("road length (km):", round(roads.length.sum() / 1000, 1))

# - Area check: Edo State 19,595 km2 from the LGA layer (UTM 31N), matches the published 19,559 km2 within 0.2%