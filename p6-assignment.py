n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    rev_a = int(str(a)[::-1])
    rev_b = int(str(b)[::-1])
    sum_rev = rev_a + rev_b
    result = int(str(sum_rev)[::-1])
    print(result)
