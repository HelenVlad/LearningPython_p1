int_ = 5  # Целочисленный тип данных
print(int_, type(int_))

float_ = 123.321  # Числа с плавающей запятой (дробные числа)
print(float_, type(float_))

bool_true = True  # Логический тип данных истина
bool_false = False   # Логический тип данных ложь
print(bool_true, bool_false, type(bool_true))

empty_tuple = ()  # Пустой кортеж
tuple_with_one_item = (1,)  # кортеж из одного элемента
tuple_ = (1, 2, "str")
print(tuple_, type(tuple_))

list_ = []  # Пустой список
chars_list = ["a", "b", "c"]
print(list_, chars_list, type(list_))

str_ = "test"  # Строковый тип данных
print(str_, type(str_))

set_ = {1, 2, 3, 1}  # Множество
empty_set = set()  # Пустое множество
print(set_, empty_set, type(set_))

dict_ = {  # словарь
    "Имя": "Вася",
    "Фамилия": "Пупкин",
    "Возраст": 18
}
empty_dict = {}  # пустой словарь
print(dict_, empty_dict, type(dict_))
