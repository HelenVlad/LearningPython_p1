salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
money_capital = 0

def need_money (spend, money_capital):
    for x in range(1, months+1):
        if x >=2:
            spend += spend * increase
        budget = salary - spend
        if budget < 0:
            money_capital += abs(budget)
    print("Какую нужно иметь сумму денег, чтобы прожить 10 месяцев, используя только эти деньги и зарплату? Ответ: ", round(money_capital,0))

need_money (6000,0)
