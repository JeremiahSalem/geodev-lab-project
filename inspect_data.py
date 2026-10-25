import csv

# with open("underservedareas.csv", encoding="utf-8-sig") as f:
#     rows = list(csv.DictReader(f))
    
# values = []
# for row in rows:
#     raw = row["building_area_sum"].strip()
#     if raw == "":
#         continue
#     values.append(float(raw))
    
# print("smallest:", min(values))
# print("largest:", max(values))
# print("count:", len(values))

def inspect_column(underservedareas, column):
    with open(underservedareas, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))
    return {
        "smallest": min(values),
        "largest": max(values),
        "count": len(values),
    }    

result = inspect_column("underservedareas.csv", "building_area_sum")
print(result)
        
    

    
