money_capital = 10000
salary = 5000 # зарплата
spend = 6000 # траты
increase = 0.05  # рост расходов

#month =   # количество месяцев, которое можно прожить
month = 1
while True:
    spend += spend*increase #
    money_capital=money_capital+salary-spend
    if money_capital > 0:
        print("В %s по счету месяце еще живем. Накопления составляют %s" % (month, round(money_capital,2)))
        month += 1
    else:
       print("В %s по счету месяце накопления закончились." % month)
       break


# TODO Оформить решение

#print(month)
