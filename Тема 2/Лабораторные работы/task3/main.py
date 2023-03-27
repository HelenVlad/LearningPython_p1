# TODO продолжить заполнение словаря
dict_hex = {
    '0x0': 0,
    '0x1': 1,
    '0x2': 2,
}

print(dict_hex)

for x in range(3, 11):
    a='0x'+ str(x)
    dict_hex[a]=x

print(dict_hex)

#строка для создания новой ветки