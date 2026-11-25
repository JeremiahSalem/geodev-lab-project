import geopandas as gpd
from shapely.geometry import Polygon
from shapely.validation import explain_validity

# ---------- Part 1: the tutor's bowtie demo ----------
bowtie = Polygon([(0, 0), (2, 2), (2, 0), (0, 2), (0, 0)])
print("valid:", bowtie.is_valid)
print("why:", explain_validity(bowtie))

layer = gpd.GeoDataFrame([{"name": "bowtie", "geometry": bowtie}], crs="EPSG:32631")
layer["geometry"] = layer.buffer(0)
print("valid now:", layer.is_valid.all())
print("why:", explain_validity(layer.geometry.iloc[0]))

# ---------- Part 2: the same checks, counted on your layers ----------
files = {
    "settlements": "data/processed/settlement_extent_urban_UTM31.gpkg",
    "study_area": "data/processed/study_area_urban_UTM31.gpkg",
    "roads": "data/processed/roads_urban_UTM31.gpkg",
    "waste_points": "data/processed/Waste_collection_point_urban_UTM31.gpkg",
}

for name, path in files.items():
    gdf = gpd.read_file(path)
    bad = ~gdf.geometry.is_valid

    print("=" * 50)
    print(name, "| rows:", len(gdf), "| invalid:", bad.sum(), "| empty:", gdf.geometry.is_empty.sum())
    print(gdf.geom_type.value_counts().to_string())

    if not bad.any():
        print("nothing to repair")
        continue

    reasons = gdf.loc[bad].geometry.apply(explain_validity).str.split("[").str[0]
    print("reasons:")
    print(reasons.value_counts().to_string())

    fixed = gdf.copy()
    fixed["geometry"] = gdf.geometry.make_valid()
    print("after make_valid -> invalid:", (~fixed.geometry.is_valid).sum(),
          "| types:", fixed.geom_type.value_counts().to_dict())

    if gdf.geom_type.isin(["Polygon", "MultiPolygon"]).all():
        buffered = gdf.copy()
        buffered["geometry"] = gdf.geometry.buffer(0)
        print("after buffer(0)  -> invalid:", (~buffered.geometry.is_valid).sum(),
              "| empty:", buffered.geometry.is_empty.sum())
        print("area after make_valid (km2):", round(fixed.area.sum() / 1_000_000, 3),
              "| after buffer(0):", round(buffered.area.sum() / 1_000_000, 3))
    else:
        print("buffer(0) skipped: it only suits polygons")