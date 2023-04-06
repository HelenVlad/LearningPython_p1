from string import ascii_letters, digits
from random import sample

lst = ascii_letters + digits
def get_random_password(n = 8) -> str:
# TODO написать функцию генерации случайных паролей
    password = sample(lst, n)
    return password

print(get_random_password())
