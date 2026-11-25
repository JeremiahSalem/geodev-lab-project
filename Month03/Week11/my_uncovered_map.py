import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from pathlib import Path

BUFFER_M = 1000  # metres; change it to the distance you want to report
UNCOVERED_COLOR = "#1FD71967"  # green; change it here for another colour

# ---------- Load ----------
lga_all = gpd.read_file("data/raw/Edo_state_LGAs.shp").to_crs(epsg=32631)
lga_all.columns = lga_all.columns.str.strip()
wards = lga_all[lga_all["lganame"].isin(["Oredo", "Egor", "Ikpoba-Okha"])][
    ["lganame", "geometry"]
].reset_index(drop=True)

facilities = gpd.read_file(
    "data/processed/Waste_collection_point_urban_UTM31.gpkg",
    layer="Waste_collection_point_urban_UTM31",
).to_crs(epsg=32631)

settlements = gpd.read_file(
    "data/processed/settlement_extent_urban_UTM31.gpkg",
    layer="settlement_extent_urban_UTM31",
)
settlements = settlements[["geometry"]].copy()
settlements["geometry"] = settlements.geometry.make_valid()

study_area = gpd.read_file("data/processed/study_area_urban_UTM31.gpkg", layer="study_area")

# ---------- Reach and uncovered areas ----------
reach = facilities[["geometry"]].copy()
reach["geometry"] = reach.buffer(BUFFER_M)
reach = reach.dissolve()

# whole-LGA version
wards["lga_area_km2"] = wards.area / 1_000_000
uncovered_lga = gpd.overlay(wards, reach, how="difference")
uncovered_lga["uncovered_km2"] = uncovered_lga.area / 1_000_000

# settlement-only version
in_lga = gpd.overlay(settlements, wards[["lganame", "geometry"]], how="intersection")
in_lga_uncovered = gpd.overlay(in_lga, reach, how="difference")
in_lga_uncovered["settlement_uncovered_km2"] = in_lga_uncovered.area / 1_000_000
uncovered_settlements = in_lga_uncovered[["lganame", "settlement_uncovered_km2", "geometry"]]

# ---------- Save the layers ----------
out_gpkg = "data/processed/uncovered_areas_UTM31.gpkg"
uncovered_lga.to_file(out_gpkg, layer="uncovered_lga", driver="GPKG")
uncovered_settlements.to_file(out_gpkg, layer="uncovered_settlements", driver="GPKG")

print("layers saved:", gpd.list_layers(out_gpkg)["name"].tolist())
print("uncovered settlement pieces:", len(uncovered_settlements),
      "| total km2:", round(uncovered_settlements["settlement_uncovered_km2"].sum(), 1))

# ---------- Map ----------
fig, ax = plt.subplots(figsize=(7, 8))
study_area.plot(ax=ax, color="white", edgecolor="#063A1B", linewidth=1.2)
in_lga.plot(ax=ax, color="#D9D9D9", linewidth=0)                       # all settlement area; grey that stays visible is covered
uncovered_settlements.plot(ax=ax, color=UNCOVERED_COLOR, linewidth=0)  # uncovered settlement area on top
wards.boundary.plot(ax=ax, color="#063A1B", linewidth=0.6)             # LGA boundaries
reach.boundary.plot(ax=ax, color="#0868AC", linewidth=1.2, linestyle="--")
facilities.plot(ax=ax, color="black", markersize=14)

km = f"{BUFFER_M / 1000:g} km"
handles = [
    Patch(facecolor=UNCOVERED_COLOR, label=f"Settlement area beyond {km}"),
    Patch(facecolor="#D9D9D9", label=f"Settlement area within {km}"),
    Line2D([0], [0], color="#0868AC", linestyle="--", label=f"{km} reach of waste points"),
    Line2D([0], [0], marker="o", color="none", markerfacecolor="black", label="Waste collection point"),
]
ax.legend(handles=handles, loc="lower left", frameon=False, fontsize=8)
ax.set_title("Settlement areas beyond reach of a waste collection point, Benin City")
ax.set_axis_off()

Path("Month03/Week11").mkdir(parents=True, exist_ok=True)
fig.savefig("Month03/Week11/uncovered_map.png", dpi=150, bbox_inches="tight")
print("map saved")