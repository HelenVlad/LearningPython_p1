def cells (number_of_cells):
    cells = {}
    for key in range(1, (number_of_cells**2)+1):
        cells[key] = 'None'
    return cells
def field (cells, number_of_cells):
    field = []
    counter = 0
    b = '+---+' * number_of_cells  # выяснить как присобачить длину строки
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

print(cells(3))
spisok = cells(3)
spisok[5] = 'X'
print(field(spisok, 3))

def players_marker():
    marker = input('Какой маркер возьмет себе Player1? Если "Х" - введите 1, если "0", то 2.\n')
    print(marker)
#players_marker()