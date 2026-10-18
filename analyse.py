with open('wards.csv') as f:
    lines = f.readlines()
    
for line in lines[1:]:
    parts = line.strip().split(",")
    ward = parts[0]
    area_km2 = float(parts[1])
    if area_km2 > 9:
        size = 'large'
    else:
        size = 'small'    
    print(ward, "is", size)
    
    
    
    
    
    
    

# for line in lines[1:]:
#     parts = line.strip().split(",")
#     ward = parts[0]
#     area_km2 = float(parts[1])
#     if area_km2 > 9:
#         size = 'large'
#     else:  # <- aligned with 'if', 4 spaces in
#         size = 'small'
#     print(ward, "is", size)  # <- also 4 spaces in, inside the loop  
    
    
    
    
    






