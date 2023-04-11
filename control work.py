def number_of_cells():
    field_size = ''.join(input('Здравствуйте, игроки! Вы запустили игру крестики-нолики. Действие игры проиходит на квадратном поле из ячеек размера N x N. Введите число N в диапазоне от 01 до 10:\n=>').split())
    lst = str(list(range(1, 11)))
    if (len(field_size) == 1 or len(field_size) == 2) and (field_size in lst):
        return int(field_size)
    else:
        print("Нет варианта ответа для выбранного значения. Выберите, пожалуйста, цифру от 1 до 10.")
        number_of_cells()

def cells(number_of_cells):
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
    marker = ''.join(input('Какой маркер возьмет себе Player1? Если "Х" - введите 1, если "0", то 2. Невыбранный символ присвоится Player2 автоматически. \n=>').split())
    players_marker_list = {}
    if len(marker) == 1 and (marker == '1' or marker == '2'):
            players_marker_list['Player1'] = 'X' if marker == '1' else '0'
            players_marker_list['Player2'] = '0' if marker == '1' else 'X'
    else:
        print("Нет варианта ответа для выбранного значения. Выберите, пожалуйста, цифру от 1 до 2.")
        players_marker()

    return players_marker_list

def first_move(): # игрок выбирает кто ходит первый
    move = ''.join(input('Кто ходит первый? Введите 1, если "Player1", если "Player2" то 2. \n=>').split())
    players_marker_list = {}
    if len(move) == 1 and (move == '1' or move == '2'):
        first_move_list = 'Player1' if move == '1' else 'Player2'
    else:
        print("Нет варианта ответа для выбранного значения. Выберите, пожалуйста, цифру от 1 до 2.")
        first_move()
    return first_move_list

def player_change(player):
    return 'Player1' if player == 'Player2' else 'Player2'

number_of_cells = number_of_cells()
players_marker_list = players_marker()
first_move = first_move()
print(field(cells(number_of_cells), number_of_cells))
