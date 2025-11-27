n = int(input())
stones_per_round = lambda i: i + 2 * i
total = 0
round_num = 1
while total < n:
    total += stones_per_round(round_num)
    round_num += 1
if (round_num - 1) % 2 == 1:
    print("Ramesh")
else:
    print("Suresh")
