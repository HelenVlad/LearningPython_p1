salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

salary_10months = salary*months
spend_10month = (spend*increase+spend)*months
budget = salary_10months-spend_10month
if budget < 0:
    need_money = abs(budget)+salary_10months  # количество денег, чтобы прожить 10 месяцев
    print("Заработанных денег не хватит. Нужно иметь накопления в размере %s. Общее количество денег, нужное, чтобы прожить 10 месяцев, составляет %s" % (round(abs(budget)), round(need_money)))
else:
    need_money = salary_10months - spend_10month
    print("Общее количество денег, нужное, чтобы прожить 10 месяцев, составляет %s" % round(need_money))
# TODO Оформить решение

#print(round(need_money))
