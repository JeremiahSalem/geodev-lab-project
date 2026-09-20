# Data notes

## Grid3 Nigeria LGA level data
-Source:- https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about 
- Downloaded: Sept 16, 2026
- 797 features, polygon
- Columns: LGA_name (Egor, Oredor, Ovia North-east, Ikoba-okha, Ohrionmwon), State (Edo State).
- No nulls in LGA name
- Covers my study area fully.
  
## OSM roads, Benin City.

- Extracted on:  Sept 16, 2026 via quickOSM, highway=*
- 30, 239 features
- Completeness: good in built up area, sparse at the edges.
- Currency:
- Positional: Roads aligns with satellite imagery, with slight systematic offset     visible.
- Attribute: only a smaller percentage carry a surface tag, so paved, unpaved, asphalt etc, cannot be separated reliably.
- fitness: adequate for access analysis in built up area, not adequate for paved-road question.


## CRS and preparation

-	All sources’ layers arrived in EPSG: 4326
-	Study area: Benin city, extracted from GRID3 LGA’s
-	 All layers clipped to the study area, then reprojected to EPSG: 32631 (UTM 31N)
-	Working files in data/processed, raw files untouched.
