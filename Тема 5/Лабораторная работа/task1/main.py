# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
dict_pattern = {'bin': None, 'dec': None, 'hex': None, 'oct': None}
# full_list = []
# for number in range(0, 16):
#     dict_number = dict_pattern.copy()
#     for func in dict_number:
#         if func == 'dec':
#             dict_number[func] = number
#         else:
#             dict_number[func] = eval(func + f'({str(number)})')
#     full_list.append(dict_number)

full_list = [{func: number if func == 'dec' else eval(func + f'({str(number)})') for func in dict_pattern} for number in range(0, 16)]

pprint(full_list)

