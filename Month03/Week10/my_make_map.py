import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from pathlib import Path

study_area = gpd.read_file("data/processed/study_area_urban_UTM31.gpkg", layer="study_area")
settlements = gpd.read_file(
    "data/processed/settlement_extent_urban_UTM31.gpkg", layer="settlement_extent_urban_UTM31"
)
waste = gpd.read_file(
    "data/processed/Waste_collection_point_urban_UTM31.gpkg", layer="Waste_collection_point_urban_UTM31"
)
roads = gpd.read_file("data/processed/roads_urban_UTM31.gpkg", layer="roads_urban_UTM31")
roads = roads[roads["highway"].notna()]  # drops rivers, pipelines and power lines

out_dir = Path("Month03/Week10")
out_dir.mkdir(parents=True, exist_ok=True)

SETTLEMENT_COLOR = "#89EAF3"
POINT_COLOR = "#E98886"
EDGE_COLOR = "#063A1B"
ROAD_COLOR = "#777777"

settlement_patch = Patch(facecolor=SETTLEMENT_COLOR, edgecolor="none", label="Settlement extent")
point_marker = Line2D([0], [0], marker="o", color="none", markerfacecolor=POINT_COLOR,
                      markeredgecolor="black", markersize=7, label="Waste collection point")
road_line = Line2D([0], [0], color=ROAD_COLOR, linewidth=1, label="Roads")

# ---------- Map 1: the whole study area (the mentor's layout) ----------
fig, ax = plt.subplots(figsize=(7, 8))
study_area.plot(ax=ax, color="white", edgecolor=EDGE_COLOR, linewidth=1)
settlements.plot(ax=ax, color=SETTLEMENT_COLOR, linewidth=0)
waste.plot(ax=ax, color=POINT_COLOR, edgecolor="black", linewidth=0.4, markersize=30)
ax.set_title("Waste collection points in Benin City (Oredo, Egor, Ikpoba-Okha)")
ax.legend(handles=[settlement_patch, point_marker], loc="lower left", frameon=False)
ax.set_axis_off()
fig.savefig(out_dir / "waste_points_map.png", dpi=150, bbox_inches="tight")

# ---------- Map 2: zoomed to where the points are ----------
fig2, ax2 = plt.subplots(figsize=(7, 8))
study_area.plot(ax=ax2, color="white", edgecolor=EDGE_COLOR, linewidth=1)
settlements.plot(ax=ax2, color=SETTLEMENT_COLOR, linewidth=0)
roads.plot(ax=ax2, color=ROAD_COLOR, linewidth=0.4)
waste.plot(ax=ax2, color=POINT_COLOR, edgecolor="black", linewidth=0.5, markersize=45)

xmin, ymin, xmax, ymax = waste.total_bounds
pad = 1500  # metres of margin around the points
ax2.set_xlim(xmin - pad, xmax + pad)
ax2.set_ylim(ymin - pad, ymax + pad)

ax2.set_title("Waste collection points in central Benin City (zoomed)")
ax2.legend(handles=[settlement_patch, road_line, point_marker], loc="lower left", frameon=False)
ax2.set_axis_off()
fig2.savefig(out_dir / "waste_points_zoom_map.png", dpi=150, bbox_inches="tight")

print("maps saved")