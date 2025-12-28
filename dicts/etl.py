legacy_data = {1: ["A"]}



base_dict = dict()
 
for i in legacy_data:
    for item in legacy_data[i]:
        base_dict[item.lower()] = i


print(base_dict)
