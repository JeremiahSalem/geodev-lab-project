# Month 1 Summary

## Question

Which part of **Benin city** are the farthest from a formal waste collection point?

## Operation

Buffered OSM waste collection points by 1km, dissolved then took the difference against settlement extent and calculated the percentage uncovered.

## Expected

With about 27,000 blobs of settlement and only a few waste collection points concentrated at the city center a buffer analysis of 1km (1000m) will cover at best 20%, another 20% partially covered and the larger percentage to be uncovered.

## Got

|SN | Statistic | Value |
|---|---|---|
|1 |Count | 26769 | 
|2 |Sum |	2.48725e+06 |
|3 |Mean |	92.9153 |
|4 |Median |	100 |
|5 |St dev  (pop) |	25.2886 |
|6 | St dev (sample) |	25.2891 |
|7| Minimum | 0 |
|8| Maximum | 100 |
 9 |Range	| 100 |
|10| Minority	| 0.00121898 |
|11| Majority |	100 |
|12| Variety |	348 |
|13| Q1 |	100 |
|14| Q3 |	100 |
|15| IQR |	0 |
|16| Missing (null) values |	0 |

## What surprised me

There are way more waste dumpsites than the few available on OSM, therefore this analysis is done tentatively to when accurate and complete data is available.

## Limitations stated plainly

-	Incompleteness of waste collection points
-	Straight line distance (as the crow flies) is an actual walking/road distance
-	Settlement type and waste collection points labels are inconsistent, so all the types are counted together.

## what I still need

-	Road network analysis to determine accurate travel distance
-	Population data to convert settlement %uncovered to population uncovered.
-	Ward level data boundary, so as to name underserved settlement by ward.
- Analyse distance in range of **the farthest, intermediate, the closest**


**Status**: Compete



