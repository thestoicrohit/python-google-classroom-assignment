a = int(input())
b = int(input())
c = int(input())
max_num = a if a > b else b
max_num = max_num if max_num > c else c
print(max_num)
