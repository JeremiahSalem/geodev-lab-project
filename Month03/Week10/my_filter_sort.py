import pandas as pd
import geopandas as gpd

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 12)

# ---------- Part 1: settlements (the tutor's ward table) ----------
gdf = gpd.read_file(
    "data/processed/settlement_extent_urban_recalc_UTM31.gpkg",
    layer="settlement_extent_urban_recalc",
)
gdf.columns = gdf.columns.str.strip()
settlements = pd.DataFrame(gdf.drop(columns="geometry"))  # plain pandas table, like the tutor's CSV

THRESHOLD = 50  # percent of a settlement's area outside the buffer

underserved = settlements[settlements["pct_uncovered"] > THRESHOLD]
print(underserved[["block_id", "total_km2", "uncovered_km2", "pct_uncovered"]].head(10))
print(f"settlements with more than {THRESHOLD}% uncovered:", len(underserved), "of", len(settlements))

ranked = settlements.sort_values("uncovered_km2", ascending=False)
print(ranked[["block_id", "total_km2", "uncovered_km2", "pct_uncovered"]].head(12))

settlements["uncovered_hectares"] = settlements["uncovered_km2"] * 100
print(settlements[["block_id", "uncovered_km2", "uncovered_hectares"]].head(3))
print("Total settlement area (km2):", round(settlements["total_km2"].sum(), 2))
print("Total uncovered area (km2):", round(settlements["uncovered_km2"].sum(), 2))
share = settlements["uncovered_km2"].sum() / settlements["total_km2"].sum() * 100
print("Uncovered share of settlement area (%):", round(share, 1))

# ---------- Part 2: roads ----------
roads_gdf = gpd.read_file("data/processed/roads_urban_UTM31.gpkg", layer="roads_urban_UTM31")
roads_gdf = roads_gdf[roads_gdf["highway"].notna()].copy()  # drops rivers, pipelines, power lines
roads_gdf["length_km"] = roads_gdf.geometry.length / 1000
roads = pd.DataFrame(roads_gdf.drop(columns="geometry"))

major = roads[roads["highway"].isin(["trunk", "primary", "secondary"])]
print(major[["full_id", "highway", "name", "length_km"]].head(10))
print("major road segments:", len(major))

print(roads["highway"].value_counts(dropna=False))
longest = roads.sort_values("length_km", ascending=False)
print(longest[["full_id", "highway", "name", "length_km"]].head(12))

print("Total road length (km):", round(roads["length_km"].sum(), 1))
print("Major road length (km):", round(major["length_km"].sum(), 1))