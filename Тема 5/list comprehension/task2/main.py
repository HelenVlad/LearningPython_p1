def list_over_for_loop(n):
    list_ = []
    for i in range(n):
        if i % 2 == 0:
            list_.append(i ** 2)

    return list_


def over_list_comprehension(n):
    return []  # TODO записать list comprehension


num = 10
print(list_over_for_loop(num))
print(over_list_comprehension(num))
