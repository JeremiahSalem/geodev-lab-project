import geopandas as gpd

BUFFER_M = 2000  # metres, same as the tutor's script

lga_all = gpd.read_file("data/raw/Edo_state_LGAs.shp").to_crs(epsg=32631)
lga_all.columns = lga_all.columns.str.strip()
lgas = lga_all[lga_all["lganame"].isin(["Oredo", "Egor", "Ikpoba-Okha"])][
    ["lganame", "geometry"]
].reset_index(drop=True)
print("urban LGAs:", lgas["lganame"].tolist())

waste = gpd.read_file(
    "data/processed/Waste_collection_point_urban_UTM31.gpkg",
    layer="Waste_collection_point_urban_UTM31",
).to_crs(epsg=32631)

# buffer operation
reach = waste.copy()
reach["geometry"] = waste.buffer(BUFFER_M)
print("buffered", len(reach), "waste points by", BUFFER_M, "m")
print("buffer area (km2):", round(reach.geometry.union_all().area / 1_000_000, 1))

# count the waste points per LGA
joined = gpd.sjoin(waste, lgas, how="inner", predicate="within")

counts = joined.groupby("lganame").size().rename("waste_point_count").reset_index()
lgas = lgas.merge(counts, on="lganame", how="left")
lgas["waste_point_count"] = lgas["waste_point_count"].fillna(0).astype(int)
print(lgas[["lganame", "waste_point_count"]])
print("Total counted:", lgas["waste_point_count"].sum(), "of", len(waste))