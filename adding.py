def add():
    my_list = []
    path = input("Введите путь к файлу: ")
    data = open(path, "r")
    for line in data:
        my_list.append(line)
    res = " ".join(my_list)
    res = res.replace(",", " ")
    res = res.replace('"',"")
    return res


