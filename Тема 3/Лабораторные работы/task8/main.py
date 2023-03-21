money_capital = 10000
salary = 5000 # зарплата
spend = 6000 # траты
increase = 0.05  # увеличение чего?

#month =   # количество месяцев, которое можно прожить

for month in range(1, 101):
    spend += spend*increase # если имеется ввиду увеличение трат
    money_capital=money_capital+salary-spend
    if money_capital > 0:
        print("В %s по счету месяце еще живем. Накопления составляют %s" % (month, round(money_capital,2)))
    else:
       print("В %s по счету месяце накопления закончились. Может стоит сменить работу?" % month)
       break


# TODO Оформить решение

#print(month)
