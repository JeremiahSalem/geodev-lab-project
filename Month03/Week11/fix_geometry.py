import geopandas as gpd 
from shapely.geometry import Polygon
from shapely.validation import explain_validity

bowtie = Polygon([(0,0), (2,2), (2,0), (0,2), (0,0)])
print("valid:", bowtie.is_valid)
print("why:", explain_validity(bowtie))

layer = gpd.GeoDataFrame([{"name": "bowtie", "geometry": bowtie}], crs="EPSG:32631")
layer["geometry"] = layer.buffer(0)
print("valid now:", layer.is_valid.all())
print("why:", explain_validity(layer.geometry.iloc[0]))