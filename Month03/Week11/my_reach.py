import geopandas as gpd

BUFFER_M = 2000  # the tutor's distance; change it to match your own threshold

# ---------- Part 1: the tutor's script, wards -> urban LGAs, facilities -> waste points ----------
lga_all = gpd.read_file("data/raw/Edo_state_LGAs.shp").to_crs(epsg=32631)
lga_all.columns = lga_all.columns.str.strip()
wards = lga_all[lga_all["lganame"].isin(["Oredo", "Egor", "Ikpoba-Okha"])][
    ["lganame", "geometry"]
].reset_index(drop=True)

facilities = gpd.read_file(
    "data/processed/Waste_collection_point_urban_UTM31.gpkg",
    layer="Waste_collection_point_urban_UTM31",
).to_crs(epsg=32631)

wards["area_km2"] = wards.area / 1000000

reach = facilities[["geometry"]].copy()
reach["geometry"] = reach.buffer(BUFFER_M)
reach = reach.dissolve()

uncovered = gpd.overlay(wards, reach, how="difference")
uncovered["uncovered_km2"] = uncovered.area / 1000000

gaps = uncovered[["lganame", "uncovered_km2"]]
result = wards.merge(gaps, on="lganame", how="left")
result["uncovered_km2"] = result["uncovered_km2"].fillna(0)
share = result["uncovered_km2"] / result["area_km2"] * 100
result["uncovered_pct"] = share.round(3)
print(result[["lganame", "area_km2", "uncovered_km2", "uncovered_pct"]].round(2))

total_share = result["uncovered_km2"].sum() / result["area_km2"].sum() * 100
print("Uncovered share of the three LGAs together:", round(total_share, 1), "%")

# ---------- Part 2: the same question, measured on settlement area only ----------
settlements = gpd.read_file(
    "data/processed/settlement_extent_urban_UTM31.gpkg",
    layer="settlement_extent_urban_UTM31",
)
settlements = settlements[["geometry"]].copy()
settlements["geometry"] = settlements.geometry.make_valid()

in_lga = gpd.overlay(settlements, wards[["lganame", "geometry"]], how="intersection")
in_lga["settlement_km2"] = in_lga.area / 1000000

in_lga_uncovered = gpd.overlay(in_lga, reach, how="difference")
in_lga_uncovered["settlement_uncovered_km2"] = in_lga_uncovered.area / 1000000

totals = in_lga.groupby("lganame")["settlement_km2"].sum().reset_index()
unc = in_lga_uncovered.groupby("lganame")["settlement_uncovered_km2"].sum().reset_index()
settle = totals.merge(unc, on="lganame", how="left")
settle["settlement_uncovered_km2"] = settle["settlement_uncovered_km2"].fillna(0)
settle["settlement_uncovered_pct"] = (
    settle["settlement_uncovered_km2"] / settle["settlement_km2"] * 100
).round(3)
print(settle.round(2))