def get_details(name, key, lst):
    for i in lst:
        if i["name"]==name:
            return i[key]