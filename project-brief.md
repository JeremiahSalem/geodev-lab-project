# My project brief

**Week1 Deliverables** GeoDev Lab Africa. Cohort one. Author: Jeremiah Salem

## The Question

>Which part of **Benin city** are the farthest from a formal waste collection point?

## Why This Question

>This question identifies formal waste collection points in the Benin city.  This shows an unequal distribution within the city. Waste management authorities, waste collectors, urban planners and the general public to establish new waste collection points, prioritize areas and organize collection routes, find the nearest waste collection points, and trace waste facilities to urban expansion. 

|SN| The Dataset |The Source |Published date |Last update |Size |
|---|---|---|---|---|---|
|1 |State boundary|[Grid3]( https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about) |December 10, 2020 at 2:00:24 AM GMT+3 |September 4, 2025 at 3:42:16 PM GMT+3 |2.6MB |
|2| LGA boundary|[Grid3]( https://data.grid3.org/datasets/GRID3::grid3-nga-operational-state-boundaries-/about) |December 4, 2020 at 2:06:50 AM GMT+3 |April 30, 2024 at 9:27:47 PM GMT+3 |645KB |
|3 |Gridded population |[Grid3]( https://data.grid3.org/maps/6966d625aea0488496d01debd3bb80f9/about) |	 August 29, 2025 at 12:00:00 AM GMT+3 |August 29, 2025 at 6:19:39 PM GMT+3 |44MB |
|4 |Waste Collection point | [OSM Api](https://overpass-turbo.eu/) |_ |_ |12KB | 
|5 |Settlement extent |[GRID3](https://data.grid3.org/datasets/GRID3::grid3-nga-settlement-extents-v4-1/about) |_ |_|2GB |
			



 To copy waste collection point data code 
 ```bash
 javascript // @name Waste collection points

[out:json][timeout:180];

// Try to resolve Edo State as an admin area (regex catches naming variants)
(
  area["name"~"Edo State|Edo"]["admin_level"="4"];
)->.edoState;

(
  // === Formal waste collection / disposal infrastructure ===

  // Designated waste disposal points (skips, communal dumpsters)
  node["amenity"="waste_disposal"](area.edoState);
  way["amenity"="waste_disposal"](area.edoState);

  // Waste transfer stations (formal municipal infrastructure)
  node["amenity"="waste_transfer_station"](area.edoState);
  way["amenity"="waste_transfer_station"](area.edoState);

  // Recycling centres/points
  node["amenity"="recycling"](area.edoState);
  way["amenity"="recycling"](area.edoState);

  // Landfills / formal dump sites
  node["landuse"="landfill"](area.edoState);
  way["landuse"="landfill"](area.edoState);

  // Waste baskets (public bins - smaller scale but still "formal" infra)
  node["amenity"="waste_basket"](area.edoState);

  // Generic dump_site tagging seen in Nigerian OSM data
  node["amenity"="dump_site"](area.edoState);
  way["amenity"="dump_site"](area.edoState);

  // Anything explicitly tagged with a waste management operator (e.g. WAMCO)
  node["operator"~"WAMCO|Waste Management",i](area.edoState);
  way["operator"~"WAMCO|Waste Management",i](area.edoState);
);

out center tags;

// ==============================================================
// FALLBACK: if the area above resolves empty (common with Nigerian
// admin boundaries in OSM), this bbox covers all of Edo State
// (south, west, north, east) and will still return results.
// Uncomment this block and comment out the area block above if
// you get zero results.
// ==============================================================

/*
[out:json][timeout:180];
(
  node["amenity"="waste_disposal"](5.6,5.0,7.6,6.8);
  way["amenity"="waste_disposal"](5.6,5.0,7.6,6.8);
  node["amenity"="waste_transfer_station"](5.6,5.0,7.6,6.8);
  way["amenity"="waste_transfer_station"](5.6,5.0,7.6,6.8);
  node["amenity"="recycling"](5.6,5.0,7.6,6.8);
  way["amenity"="recycling"](5.6,5.0,7.6,6.8);
  node["landuse"="landfill"](5.6,5.0,7.6,6.8);
  way["landuse"="landfill"](5.6,5.0,7.6,6.8);
  node["amenity"="waste_basket"](5.6,5.0,7.6,6.8);
  node["amenity"="dump_site"](5.6,5.0,7.6,6.8);
  way["amenity"="dump_site"](5.6,5.0,7.6,6.8);
  node["operator"~"WAMCO|Waste Management",i](5.6,5.0,7.6,6.8);
  way["operator"~"WAMCO|Waste Management",i](5.6,5.0,7.6,6.8);
);
out center tags;
*/
```


## Description

>Over the 12 months of the bootcamp, I’ll be building a decision support platform for assessing accessibility to waste collection facilities in Benin city.

**Status** Week1 complete. Data acquisition in week 2, see [Data-note.md](Data-notes.md) 