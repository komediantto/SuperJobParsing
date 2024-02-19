def filter_names(names):
    name_list = []
    unique_list_names = []
    for full_name in names:
        name_parts = full_name.split()
        if len(name_parts) == 1:
            continue
        name_list += [sorted(name_parts)]
    print(name_list)
    for name in name_list:
        new_dict = {}
        new_dict[name[0]] = name[1:]
        unique_list_names.append(new_dict)

    filtered_data = {}

    for item in unique_list_names:
        for key, value in item.items():
            if key in filtered_data:
                if len(value) > len(filtered_data[key]):
                    filtered_data[key] = value
            else:
                filtered_data[key] = value

    new_list_names = []
    for key, values in filtered_data.items():
        new_list_names.append(f"{key} " + " ".join(values))
    print(new_list_names)


# Пример использования:
names = [
    "Иванов Илья Сергеевич",
    "Иванов Илья",
    "Илья Иванов",
    "Илья",
    "Егоров Андрей Михайлович",
    "Андрей",
    "Егоров Андрей",
    "Михаил Сергеевич",
    "Сергеевич Михаил",
]
print(filter_names(names))
