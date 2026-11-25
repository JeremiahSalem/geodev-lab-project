import rasterio

with rasterio.open("data/raw/dem.tif") as src:
    x,y = src.xy(0,0)
    print("Centre of the top-left pixel:", round(x,1), round(y,1))
    
    row,col = src.index(600000, 820000)
    print("That location is row", row, "column is", col)