import geopandas as gpd 

def main():
    gdf = gpd.read_file("africa.json")
    print(gdf.shape)
    print(gdf.head()) 

if __name__ == '__main__':
    main()