import pandas as pd
import geopandas as gpd

wards = gpd.read_file("data/processed/wards.gpkg", layer="wards")
pop = pd.read_csv("data/raw/ward_population.csv")

first_try = wards.merge(pop, left_on="ward_name", right_on="ward", how="left")
matched = first_try["population_2024"].notna().sum()
print("matched on first try:", matched, "of", len(wards))

def clean_name(series):
    return (
        series.astype("string")
        .str.strip()
        .str.upper()
        .str.replace(r"[-'’]", " ", regex=True)
        .str.replace(r"\s+", " ", regex=True)
    )

wards["join_key"] = clean_name(wards["ward_name"])
pop["join_key"] = clean_name(pop["ward"])

print("duplicate keys in wards:", wards["join_key"].duplicated().sum())
print("duplicate keys in pop:", pop["join_key"].duplicated().sum())

joined = wards.merge(pop, on="join_key", how="left")
matched = joined["population_2024"].notna().sum()
print("matched after cleaning:", matched, "of", len(wards))
print("rows after join:", len(joined), "(should equal", len(wards), ")")

print("unmatched wards:")
print(joined.loc[joined["population_2024"].isna(), "ward_name"].to_list())











# import pandas as pd
# import geopandas as gpd

# wards = gpd.read_file("data/processed/wards.gpkg", layer="wards")
# pop = pd.read_csv("data/raw/ward_population.csv")

# first_try = wards.merge(pop, left_on="ward_name", right_on="ward", how="left")
# matched = first_try["population_2024"].notna().sum()
# print("matched on first_try:", matched, "of", len(wards))

# def clean_name(name):
#     return name.strip().upp().replace("-"," ")

# wards["join_key"] = wards["ward_name"].apply(clean_name)
# pop["join_key"] = pop["ward"].apply(clean_name)

# joined = wards.merge(pop, on="join_key", how="left")
# matched = joined["population_2024"].notna().sum()
# print("matched after cleaning:", matched, "of", len(wards))
# print(joined[["ward_name", "population_2024"]])
