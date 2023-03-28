# TODO продолжить заполнение словаря
dict_hex = {
    '0x0': 0,
    '0x1': 1,
    '0x2': 2,
}

print(dict_hex)

for x in range(3, 16):
    a = list(hex(x))
    a[-1] = str.upper(a[-1])
    a="".join(a)
    dict_hex[a] = x

print(dict_hex)
