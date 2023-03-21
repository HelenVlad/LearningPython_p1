# TODO Вынести константу pi


# TODO убрать аргумент pi из функций и заменить его на константу из глобальной области видимости
def square_circle(r, pi):
    return pi * r ** 2


def length_circle(r, pi):
    return 2 * pi * r


radius = 8  # радиус круга
# TODO подправить передаваемые аргументы
square = square_circle(radius, 3.14)
length = length_circle(radius, 3.14)

print("Площадь равна =", square)
print("Длина окружности равна =", length)
