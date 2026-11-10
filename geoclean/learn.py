# This line is a comment. python ignores it.
# print('Hello from Ibadan')
# print(28454*100)
# print(10/4)  

# state = 'oya'
# print(state)
# state = 'Lagos'
# print(state)

# population = 5580894
# buffer_distance =500
# ward_name = 'Bodija'
# print(ward_name, buffer_distance) 

# ward_name = 'Bodija'
# ward_count = 774
# area_km = 3080.5
# is_capital = False
# print(type(ward_name), type(ward_count), type(area_km), type(is_capital)) 

# case_1 = 5 + 5
# case_2 = "5" + "5" 
# case_3 = "ibadan" + " north"
# print(case_1, case_2, case_3)

# area_text = "12.4"
# area_number = float(area_text)
# print(area_number * 100)

#LISTS
# wards = ["Agodi", "Bashorun", "Dugbe", "Molete"]
# print(wards)
# print(len(wards))
# print(wards[0])
# print(wards[1])
# wards.append('Oje')
# print(wards)

# wards = ["Agodi", "Bodija", "Sabo"]

# for ward in wards:
#     print("checking", ward)

# areas = [28454, 3345, 20131] #Oya, Lagod, and Kano in sqkm
# for area in areas:
#     hectares = area * 100
#     print(area, "square kilometers", hectares, "hectares")
#     print("Done!")

# area = 28454

# if area > 20000:
#     print(area, ' is large')
# elif area > 5000:
#     print(area, 'is medium')
# else:
#     print(' is small')

#comparison
# state = "Oyo"
# print(state == "Oyo")
# print(state == "Lagos")
# print(state != "Lagos")

# Oyo_hectares = 28454 * 100
# Lagos_hectares = 3345 * 100
# Kano_hectares = 20131 * 100

# def km2_to_hectares(area):
#     return area * 100

# print(km2_to_hectares(28454))
# print(km2_to_hectares(3345))
# print(km2_to_hectares(20131))

def describe(name, count):
    return name + "has " +str(count) + "wards."

print(describe("Ibadan North", 12))