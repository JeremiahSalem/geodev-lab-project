# Data Preparation

**Week3 Deliverables** GeoDev Lab Africa. Cohort one. Author: Jeremiah Salem

What i reprojected, what i clipped, what i checked, and what i fixed

## Coordinate system decisions

Working CRS:EPSG: 32631 (UTM 31N)

**Why this one**: My project requires both area and distance calculations, therefore my chosen CRS:EPSG: 32631 is in meters and study area falls in UTM zone 31N 

|SN |Dataset |CRS as downloaded |CRS after |Operation |
|---|---|---|---|---|
|1 |Study area boundary| EPSG:4326|EPSG: 32631 |Reprojected and Exported to layer |
|2 |LGA area boundary| EPSG:4326|EPSG: 32631 |Reprojected and Exported clipped to study area boundary layer |
|3 |OSM Roads| EPSG:4326|EPSG: 32631 |Reprojected and Exported clipped to study area boundary layer |
|4 |Settlement extent| EPSG:4326|EPSG: 32631 |Reprojected and Exported clipped to study area boundary layer |
|5 |Waste collection points| EPSG:4326|EPSG: 32631 |Reprojected and Exported clipped to study area boundary layer |
 
 ## Clipping to the study area

 - Boundary used: Oredo, Egor, Ikpoba-okha, Ovia-northeast and Uhunmwonde LGAs 

 - Features before clipping: Edo-state LGAs, GRID3_NGA_settlement_extents_4, waste_collection_points, Benin_roads.

 - Features after clipping: Benin_city_UTM31, settlement_extent_UTM31, waste_collection_points, Roads. respectively.

 ## The five quality checks

|SN |Check |Result |Action taken |
|---|---|---|---|
|1 | Are the dataset what i think it is |yes |None |
|2 |Are there nulls in the fields i need |yes |None |
|3 |Are there duplicate features |yes |Removed duplicate |
|4 |Are the geometry valid |yes |None |
|5 |Does the coverage span the whole study area |yes |None |

## The problems found, and what i did
**Problem** Incomplete waste collection points, null values in the field i needed, both of which are flagged. And remove duplicate road features.

 
## Analysis Ready output

-	All sources’ layers arrived in EPSG: 4326
-	 All layers clipped to the study area, then reprojected to EPSG:32631 (UTM 31N)
-	Working files in [data/processed](../Month1/Data), raw files untouched.


**Status** week3 complete. Next-up [first spatisl analysis](week4.md)  
