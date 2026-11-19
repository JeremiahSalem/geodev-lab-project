import geopandas as gpd

points = gpd.read_file("data/raw/Waste_collection_Points_Benin_City.shp")
print(points.columns.tolist())
print(points.crs)
print(len(points))

points = points.to_crs("EPSG:4326")
points["longitude"] = points.geometry.x
points["latitude"] = points.geometry.y

table = points.drop(columns="geometry")
table.to_csv("data/raw/waste_collection_points.csv", index=False)
print("saved", len(table), "rows")