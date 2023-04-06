from random import shuffle, randint
def get_unique_list_numbers() -> list[int]:
# TODO написать функцию для получения списка уникальных целых чисел
    list_ = list(range(-10, 11))
    shuffle(list_)
    while True:
        list_.pop(randint(0, len(list_)-1))
        if len(list_) == 15:
            break
    return list_

print(get_unique_list_numbers())
list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
