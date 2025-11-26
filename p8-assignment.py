n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    last_digit = (a % 10)
    result = pow(last_digit, b % 4 if b % 4 != 0 else 4, 10)
    print(result)
