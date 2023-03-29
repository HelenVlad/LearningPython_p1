main_str_ = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
def get_count_char(main_str): # TODO посчитать количество каждой буквы в строке в аргументе str_
    list_of_letters = list(''.join(filter(str.isalpha, main_str.lower())))
    """текст приведен к нижнему регистру через lower, затем из текста удалены все небуквенные значения через ф-ю filter и isalpha, 
    затем текст переведен побуквенно в список с помощью list """
    dictionary = {}
    for character in list_of_letters:
        if character in dictionary:
            dictionary[character] += 1
        else:
            dictionary[character] = 1
    return dictionary
print("Количественная статистика по частоте cимволов в веденном тексте:", get_count_char(main_str_), sep='\n')

def percent(dictionary):
    sum_value = sum(dictionary.values())
    for obj in dictionary:
        value = dictionary[obj]
        dictionary[obj] = str(round((value/sum_value)*100, 1))+"%"
    return dictionary
print("Процентная статистика по частоте cимволов в веденном тексте:", percent(get_count_char(main_str_)), sep='\n')