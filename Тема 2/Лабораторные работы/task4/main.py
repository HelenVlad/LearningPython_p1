BYTES_ONE_CHAR = 1  # размер одного символа в байтах

# никаких магических чисел
pages = 10 # TODO ввести количество страниц
lines = 50   # TODO ввести количество строк
chars = 150   # TODO ввести количество символов в строке

total_chars = chars*lines*chars  # TODO общее количество символов в книге
total_bytes = total_chars*BYTES_ONE_CHAR  # TODO размер одной книги в байтах

disk_size = 1457664  # TODO размер дискеты в байтах

print(disk_size//total_bytes)     # TODO найти количество книг, которое поместится на дискете
