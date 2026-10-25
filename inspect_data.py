import csv

def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    values = []
    for row in rows:
        raw = row[column].strip()
        if raw  == "":
            continue
        values.append(float(raw))

    return{
        "smallest":min(values),
        "largest":max(values),
        "count":len(values)
    }

area_sum_result = inspect_column("underservedareas.csv", "building_area_sum")
print("Building Area Sum:", area_sum_result)
building_count_result = inspect_column("underservedareas.csv", "building_count")
print("Building Count:", building_count_result)
        
