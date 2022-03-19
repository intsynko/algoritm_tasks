places = [
    {"Id": 0, "Name": "Ukraine"},
    {"Id": 1, "Name": "Armenia"},
    {"Id": 2, "Name": "Russia"},
    {"Id": 3, "Name": "Petersburg", "ParentId": 2},
    {"Id": 4, "Name": "Mariburg", "ParentId": 5},
    {"Id": 5, "Name": "Lvov", "ParentId": 0},
    {"Id": 6, "Name": "Erevan", "ParentId": 1},
    {"Id": 23, "Name": "Pushkin", "ParentId": 3},
    {"Id": 12, "Name": "Sortov", "ParentId": 5},
    {"Id": 92, "Name": "Zradov", "ParentId": 12}
]


places_dict = {i["Id"]: i for i in places}


def build_path(item):
    return (item.get('ParentId') is not None and build_path(places_dict[item.get('ParentId')]) or []) + [item["Name"]]


def check_city(toponim: str):
    return [build_path(i) for i in places_dict.values() if toponim in i['Name']]


assert build_path({"Id": 12, "Name": "Sortov", "ParentId": 5}) == ["Ukraine", "Lvov", "Sortov"]

assert check_city("ov") == [["Ukraine", "Lvov"],
                          ["Ukraine", "Lvov", "Sortov"],
                          ["Ukraine", "Lvov", "Sortov", "Zradov"]]
