n = int(input())
for i in range(n):
    row = []
    for j in range(i + 1):
        if j == 0 or j == i:
            row.append(1)
        else:
            prev_row = []
            for k in range(i):
                if k == 0 or k == i - 1:
                    prev_row.append(1)
                else:
                    prev_row.append(0)
            row.append(prev_row[j - 1] + prev_row[j])
    print(' '.join(map(str, row)))
