t = int(input())
for i in range(t):
    n = int(input())
    max_cakes = 0
    for a in range(1, n + 1):
        if n % a == 0:
            leftover = n - (n // a) * a
            eaten = n - leftover
            if eaten > max_cakes:
                max_cakes = eaten
    print(n // 2 if n > 1 else 0)
