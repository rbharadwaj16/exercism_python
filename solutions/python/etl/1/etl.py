def transform(legacy_data):
    base_dict = dict()

    for i in legacy_data:
        for item in legacy_data[i]:
            base_dict[item.lower()] = i

    return base_dict
