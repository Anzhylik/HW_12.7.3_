per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
print(per_cent)
money = int(input("Введите сумму вклада - "))
deposit = []
deposit.append(int(money*per_cent["ТКБ"]/100))
deposit.append(int(money*per_cent["СКБ"]/100))
deposit.append(int(money*per_cent["ВТБ"]/100))
deposit.append(int(money*per_cent["СБЕР"]/100))
print(deposit)
max_deposit = max(deposit)
print("Максимальная сумма, которую вы можете заработать - " + str(max_deposit))