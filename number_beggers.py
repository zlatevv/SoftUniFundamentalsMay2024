money = input().split(", ")
beggers = int(input())
money_integer = []
for m in money:
    money_integer.append(int(m))
start_index = 0
final_money = []
for begger in range(beggers):
    total = 0
    for index in range(start_index, len(money_integer), beggers):
        total += money_integer[index]
    final_money.append(total)
    start_index += 1
print(final_money)