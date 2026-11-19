import geopandas as gpd

BUFFER_M = 1000  # set this to the buffer distance you used in QGIS, in metres

settlements = gpd.read_file("data/processed/settlement_extent_urban_UTM31.gpkg")
waste = gpd.read_file("data/processed/Waste_collection_point_urban_UTM31.gpkg")

settlements.columns = settlements.columns.str.strip()

# keep only polygons (a clip can leave stray lines or points on the boundary)
settlements = settlements[settlements.geom_type.isin(["Polygon", "MultiPolygon"])]

# drop the old area columns on this copy; the original file is untouched
stale = [c for c in settlements.columns if "km2" in c or "uncovered" in c]
print("dropping stale columns:", stale)
settlements = settlements.drop(columns=stale).reset_index(drop=True)

settlements["total_km2"] = settlements.geometry.area / 1_000_000

buffer_zone = waste.geometry.buffer(BUFFER_M).union_all()
uncovered = settlements.geometry.difference(buffer_zone)
settlements["uncovered_km2"] = uncovered.area / 1_000_000
settlements["pct_uncovered"] = settlements["uncovered_km2"] / settlements["total_km2"] * 100

print(settlements["pct_uncovered"].describe())
print("fully covered (0%):", (settlements["pct_uncovered"] == 0).sum())
print("fully uncovered (100%):", (settlements["pct_uncovered"] >= 99.999).sum())

settlements.to_file(
    "data/processed/settlement_extent_urban_recalc_UTM31.gpkg",
    layer="settlement_extent_urban_recalc",
    driver="GPKG",
)
print("saved", len(settlements), "settlements")