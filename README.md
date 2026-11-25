# My Geodev Lab Africa project

>This project identifies formal waste collection points in the Benin city.  This shows an unequal distribution within the city. Waste management authorities, waste collectors, urban planners and the general public to establish new waste collection points, prioritize areas and organize collection routes, find the nearest waste collection points, and trace waste facilities to urban expansion. 

## The Question

>Which part of Benin city are the farthest from a formal waste collection point? 

Built over twelve months with Geodev Lab Africa, cohort one.

## Progress

- [x] Week1; Project brief with a source link for every dataset
- [x] Week2; Data Downloaded, opened and described
- [x] Week4; Reprojected, clipped and quality checked
- [x] Week5; First spatial analysis 

## Month 2: Python Foundations

- [x] Week6; set the project with uv and added pandas. [check.py](geoclean\check.py) prints pandas version
- [x] Week7; [analyse.py](analyse.py) reads [wards.csv](wards.csv) , converts each area and classifies each ward.
- [x] Week8; [inspect_data.py](inspect_data.py) summarises Building Area Sum and Building count in my data.
- [x] Week9; Consolidation and refactoring of week8 code

### Month 2 Reflection

>This week 9 finally gave clarity to what I was doing for the last three weeks, separating my code into small functions that does one clear job, easy to name, understand and fix made the difference. I'll review the past weeks with this understanding and see what comes out.

## Month 2: Geospatial Python Automation
- [x] Week10; Geopandas Loaded, checked, joined and mapped waste collection points, Benin city.
- [x] week11; CRS checks and spatial resolution

### CRS
All raw layers arrived in EPSG:4326. I reprojected everything to EPSG:32631 (WGS 84 / UTM zone 31N).
estimate_utm_crs() suggested the same code, and Benin City (about 5.6 E) lies inside zone 31N (0 to 6 E).
Edo State straddles 6 E, so the far east of the state is slightly more distorted, but the study area is not affected.
Check: the LGA layer gives Edo State as 19,595 km2, within about 0.2% of the published 19,559 km2.

### Results
- Points per LGA (my_count.py): Oredo 34, Egor 4, Ikpoba-Okha 0. Total counted: 38 of 38.
- Coverage gap (my_reach.py), 2,000 m buffer around the waste points: 93.7% of the three LGAs lies beyond the buffer.
  Measured on settlement area only, 84.5% lies beyond it (Oredo 60.7%, Egor 81.2%, Ikpoba-Okha 96.4%).
- Geometry validity (my_validity.py): 0 invalid geometries in settlements, study area, roads and waste points. No repair was needed.

### Why 2,000 m
2,000 m is the outer limit of the accessibility bands I use in this project (0-500 m, 500 m-1 km, 1-2 km, over 2 km),
so anything beyond it counts as potentially underserved. It is my own threshold, not an official standard.

### Outputs
- data/processed/uncovered_areas_UTM31.gpkg (layers: uncovered_lga, uncovered_settlements)
- Month03/Week11/uncovered_map.png

### Limitation
The analysis rests on 38 OpenStreetMap waste collection points, all in Oredo and Egor, inside a box of about 5.3 km by 6.9 km.
Ikpoba-Okha has none, yet it is about 70% of the study area, so its 0 count more likely reflects unmapped points than absent service.
The buffer also measures straight-line distance, not walking or road distance, so real access is probably worse than shown.
The percentages describe where OSM has mapped points as much as where service exists.


See [project-brief.md](project-brief.md) for the full brief.
