def number_of_cells(): #Ф-я запрашивает размер поля
    field_size = ''.join(input('\nВведите число N (количество клеток по горизонтали и вертикали) в диапазоне от 03 до 10:\n=>').split())
    lst = [str(number) for number in range(3, 11)]
    if field_size in lst:
        return int(field_size)
    else:
        print("Нет варианта ответа для выбранного значения. Выберите, пожалуйста, цифру от 03 до 10.")
        return number_of_cells()


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
    while True:
        marker = ''.join(input('Какой знак возьмет себе Player1? Если "Х" - введите 1, если "0", то 2. Невыбранный символ присвоится Player2 автоматически. \n=>').split())
        players_marker_list = []
        lst = ['1', '2']
        if marker in lst:
            players_marker_list.append(('Player1', 'X')) if marker == '1' else players_marker_list.append(('Player1', '◯'))
            players_marker_list.append(('Player2', '◯')) if marker == '1' else players_marker_list.append(('Player2', 'X'))
            return players_marker_list  # список, в котором хранится 2 кортежа в виде [(наименование_игрока, маркер), (наименование_игрока, маркер)]
        else:
            print("Нет варианта ответа для выбранного значения. Выберите, пожалуйста, цифру от 1 до 2.")

def first_move(players_marker): #игрок выбирает кто ходит первый
    while True:
        move = ''.join(input('Кто ходит первый? Введите 1, если "Player1", если "Player2" то 2. \n=>').split())
        if move == '1':
            first_move_list = players_marker[0]
            return first_move_list  # возвращает кортеж вида (наименование_игрока_который_ходит_первым, маркер)
        elif move == '2':
            first_move_list = players_marker[-1]
            return first_move_list  # возвращает кортеж вида (наименование_игрока_который_ходит_первым, маркер)
        else:
            print("Нет варианта ответа для выбранного значения. Выберите, пожалуйста, цифру от 1 до 2.")

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


def transpose_matrix(matrix):
    trans = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return trans
def check_line(matrix):
    for lst in matrix:
        if len(set(lst)) == 1:
            return True

def diagonal(matrix):
    diagonal1 = [matrix[j][j] for j in range(len(matrix))]
    i = len(matrix)-1
    diagonal2 = []
    for j in range(len(matrix)):
        diagonal2.append(matrix[j][i])
        i -= 1
    diagonal = [diagonal1, diagonal2]
    return diagonal

def check_win(cells):
    def matrix(cells):
        value = list(cells.values())
        length = len(value)
        middle_index = round(length ** 0.5)
        lst = []
        for x in range(0, length, middle_index):
            lst.append(value[x: middle_index + x])
        return lst
    return True if any([check_line(matrix(cells)), check_line(transpose_matrix(matrix(cells))), check_line(diagonal(matrix(cells)))]) is True else False

def game():
    print("Привет! Вы запустили игру крестики-нолики. Действие игры происходит на квадратном поле из ячеек размера N x N.\n\
Игроки по очереди ставят на свободные ячейки поля знаки (один всегда крестики, другой всегда нолики).\n\
Первый, выстроивший в ряд свои фигуры по вертикали, горизонтали или большой диагонали, выигрывает.\n")
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
            current_player = player_change(move_made, players_marker_list)
            cells_ = players_move(current_player, cells_)
            move_made = current_player
        if counter == len(cells_):
            print(field(cells_, number_of_cells_))
            print('Игра окончена.')
            break

# markers = [('Player1', '✘'), ('Player2', '◎')]
# first_move_ = ('Player2', '✘')

cells_ = cells(3)

cells_[1] = '0'
cells_[2] = '0'
cells_[3] = 'X'
cells_[4] = 'X'
cells_[5] = '0'
cells_[6] = '0'
cells_[7] = 'X'
cells_[8] = 'X'
cells_[9] = '0'

# cells_[1] = '1'
# cells_[2] = '2'
# cells_[3] = '3'
# cells_[4] = '4'
# cells_[5] = '5'
# cells_[6] = '6'
# cells_[7] = '7'
# cells_[8] = '8'
# cells_[9] = '9'

# matrix_ = matrix(cells_)
# print('Матрица выглядит:', matrix_)
#
# print('Транспонированная матрица выглядит:', transpose_matrix(matrix_))

print('Чек выигрыша:', check_win(cells_))
