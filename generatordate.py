
def in_user():

    num = int(input("Введите количество добавляемых элементов: "))
    n = 1
    list_name = []
    while n <= num:
        nm = str(input("Введите имя:"))
        list_name.append(nm)
        surname = str(input("Введите фамилию:"))
        list_name.append(surname)
        call = str(input("Введите номер: "))
        list_name.append(call)
        n += 1
    
    return " ".join(list_name)
