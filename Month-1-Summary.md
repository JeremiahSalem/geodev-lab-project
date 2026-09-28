# Month 1 Summary

## Question

Which part of Benin city are the farthest from a formal waste collection point?

## Operation

Buffered OSM waste collection points by 1km, dissolved then took the difference against settlement extent and calculated the percentage uncovered.

## Expected

With about 27,000 blobs of settlement and only a few waste collection points concentrated at the city center a buffer analysis of 1km (1000m) will cover at best 20%, another 20% partially covered and the larger percentage to be uncovered.

## Got
Statistic	Value
Count	26769
Sum	2.48725e+06
Mean	92.9153
Median	100
St dev (pop)	25.2886
St dev (sample)	25.2891
Minimum	0
Maximum	100
Range	100
Minority	0.00121898
Majority	100
Variety	348
Q1	100
Q3	100
IQR	0
Missing (null) values	0

## What surprised me

There are way more waste dumpsites than the few available on OSM, therefore this analysis is done tentatively to when accurate and complete data is available.

## Limitations stated plainly

-	Incompleteness of waste collection points
-	Straight line distance (as the crow flies) is an actual walking/road distance
-	Settlement type and waste collection points labels are inconsistent, so all the types are counted together.
-	
## what I still need

-	Road network analysis to determine accurate travel distance
-	Population data to convert settlement %uncovered to population uncovered.
-	Ward level data boundary, so as to name underserved settlement by ward.




