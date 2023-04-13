# def dict_to_list(dict): # преобразует словарь с одним элементом в список с двумя элементами
#     items = list(dict.items())[0]
#     items = (items[0], items[1])
#     return items
def number_of_cells(): #Ф-я запрашивает размер поля
    print("Привет! Вы запустили игру крестики-нолики. Действие игры происходит на квадратном поле из ячеек размера N x N.\n\
Игроки по очереди ставят на свободные ячейки поля знаки (один всегда крестики, другой всегда нолики).\n\
Первый, выстроивший в ряд свои фигуры по вертикали, горизонтали или большой диагонали, выигрывает.")
    while True:
        field_size = ''.join(input('Введите число N (количество клеток по горизонтали и вертикали) в диапазоне от 03 до 10:\n=>').split())
        lst = str(list(range(1, 11)))
        if (len(field_size) == 1 or len(field_size) == 2) and (field_size in lst):
            return int(field_size)
        else:
            print("Нет варианта ответа для выбранного значения. Выберите, пожалуйста, цифру от 1 до 10.")

def cells(number_of_cells): #ф-я принимает размер поля в виде целочисленного значения number_of_cells,
    # затем генерирует словарь соответствующего размера.
    cells = {}
    for key in range(1, (number_of_cells**2)+1):
        cells[key] = 'None'
    return cells

def field(cells, number_of_cells): #функция рисующая поле
    field = []
    counter = 0
    b = '+---+' * number_of_cells
    for lst in cells:
       if counter % number_of_cells == 0:
           field.append(f'\n{b}\n')
       counter += 1
       if cells.get(lst) == 'None':
           if lst > 9:
               field.append(f'|{lst} |')
           else: field.append(f'| {lst} |')
       else:
           field.append(f'| {cells.get(lst)} |')
    field.append(f'\n{b}\n')
    return "".join(field)

def players_marker(): #игрок выбирает себе маркер
    marker = ''.join(input('Какой знак возьмет себе Player1? Если "Х" - введите 1, если "0", то 2. Невыбранный символ присвоится Player2 автоматически. \n=>').split())
    players_marker_list = []
    if len(marker) == 1 and (marker == '1' or marker == '2'):
            players_marker_list.append(('Player1', '⨉')) if marker == '1' else players_marker_list.append(('Player1', '◯'))
            players_marker_list.append(('Player2', '◯')) if marker == '1' else players_marker_list.append(('Player2', '⨉'))
    else:
        print("Нет варианта ответа для выбранного значения. Выберите, пожалуйста, цифру от 1 до 2.")
        players_marker()

    return players_marker_list # список, в котором хранится 2 кортежа в виде [(наименование_игрока, маркер), (наименование_игрока, маркер)]

def first_move(players_marker): #игрок выбирает кто ходит первый
    while True:
        move = ''.join(input('Кто ходит первый? Введите 1, если "Player1", если "Player2" то 2. \n=>').split())
        first_move_list = []
        if len(move) == 1 and (move == '1' or move == '2'):
            if move == '1':
                first_move_list = players_marker[0]
            else:
                first_move_list = players_marker[-1]
        else:
            print("Нет варианта ответа для выбранного значения. Выберите, пожалуйста, цифру от 1 до 2.")
        return first_move_list #возвращает кортеж вида (наименование_игрока_который_ходит_первым, маркер)

def player_change(player, players_marker_list):
    if player[0] == 'Player1':
        return players_marker_list[-1] # ('Player2', '*')
    else:
         return players_marker_list[0] # ('Player1', '*')

def players_move(current_player, cells):
    while True:
        answer = ''.join(input(f'Твой ход, {current_player[0]}! Выбери число, соответствующее ячейке, от 1 до {len(cells)}.\n=>').split())
        lst = str(list(range(1, len(cells)+1)))
        if answer in lst:
            if cells[int(answer)] == 'None':
                cells[int(answer)] = current_player[-1]
                return cells
            else:
                print(f'Данная ячейка занята. Пожалуйста, выберите свободную ячейку.')
        else:
            print(f'Нет варианта ответа для выбранного значения. Выберите, пожалуйста, цифру от 1 до {len(cells)}.')

def game():
    number_of_cells_ = number_of_cells() # спрашиваем о размере поля, сохр в переменную
    players_marker_list = players_marker() #спрашиваем о том, кто каким маркером играет, сохр в переменную
    first_move_ = first_move(players_marker_list) #спрашиваем, кто ходит первый,  сохр в переменную
    cells_ = cells(number_of_cells_) #создаем в памяти список с ячейками заданной длинны
    counter = 0
    move_made = []
    while True:
        print(field(cells_, number_of_cells_))
        if counter == 0:
            cells_ = players_move(first_move_, cells_) # игрок сделал ход, измененное поле записывается в переменной
            move_made = first_move_
            counter +=1
        else:
            counter +=1
            print(move_made, players_marker_list)
            current_player = player_change(move_made, players_marker_list)
            print(current_player)
            cells_ = players_move(current_player, cells_)
            move_made = current_player
        if counter == len(cells_):
            print(field(cells_, number_of_cells_))
            print('Игра окончена.')
            break

# markers = [('Player1', '✘'), ('Player2', '◎')]
# first_move_ = ('Player2', '✘')
# player_change_ = player_change(first_move_, markers)
#
# cells_ = cells(3)
#
# print(players_move(first_move_, cells_))
game()