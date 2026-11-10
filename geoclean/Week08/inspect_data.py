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

def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
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
        "average": sum(values) / len(values)
    }    

area_sum_result = inspect_column("underservedareas.csv", "building_area_sum")
building_count_result = inspect_column("underservedareas.csv", "building_count")

print("Building area sum:", area_sum_result)
print("Building count:", building_count_result)
        
    

    
