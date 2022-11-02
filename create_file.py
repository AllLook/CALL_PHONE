import sys
sys.path.append(r"..\ call_phone")
import csv
import generatordate as gn
import adding as ad

list_user = input(
       "Введите список абонентов в формате: фамилия(пробел) имя(пробел) номер(пробел): (если списка нет введите NO или FILE(чтобы выполнить из файла)) : \n ").strip()
if list_user == "NO":
        list_user = gn.in_user()
print(list_user)

if list_user == "FILE":
        list_user = ad.add()

list_us = list_user.split()
print(list_us)

with open("call_file.csv", "a", encoding="windows-1251", newline="") as file:
    writer = csv.writer(file)
    list_header = ["name", "surname", "numbers"]
    am_header = len(list_header)  # длина заголовков для размера подсписков
    writer.writerow(list_header)
    for us in range(0, len(list_us), am_header):  # шаг на нужное кол-во элементов
        writer.writerow(list_us[us:us + am_header])# текущий шаг от текущего до
file.close()