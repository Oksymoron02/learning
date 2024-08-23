balance = 70000
for_hour = 10
time_for_day = 4
bet_for_day = for_hour * time_for_day
goal = 100000

days = 0

while balance < goal:
    bet = balance // 1000
    win_daily = bet_for_day * bet
    balance += win_daily
    days += 1

print(days, balance)