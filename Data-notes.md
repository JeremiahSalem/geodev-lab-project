# Data notes

**Week2 Deliverables** GeoDev Lab Africa. Cohort one. Author: Jeremiah Salem

What I downloaded, where it came from, what is in it, and what is wrong with it.

|SN |Dataset |Source |Features |Date |Comment |Size |
|---|---|---|---|---|---|---|
|1 |LGA boundary.shp |[GRID3](https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about) |(polygon) 774 |Sept |No nulls in LGA ,Covers my study area fully|645KB |
|2 |OSM Roads.shp |QuickOSM |(line) 56,061 |Sept |Many have no surface tag, so paved and unpaved cannot be separated everywhere,Coverage looks good in built-up area, sparse at the edges.
|3 |Settlement extent.gpkg |[GRID3](https://data.grid3.org/datasets/GRID3::grid3-nga-settlement-extents-v4-1/about) |(blobs)>20000 |sept |null values present  |2GB |
|4 |State boundary.shp |[GRID3](https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about) |(polygon)36 |Sept |ok |2.6MB |
|5 |Waste Collection point.kml | [OSM Api](https://overpass-turbo.eu/) |(point)38 |Sept |null values present, incomplete waste collection points since both formal and informal waste points are counted together |12KB | 

**Status** Week2 complete. Reprojection and quality checks in week 3, see [Data-preparation.md](Data.preparation.md)  




