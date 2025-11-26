n = int(input())
for i in range(n):
    sh, sm, eh, em = map(int, input().split())
    total_start = sh * 60 + sm
    total_end = eh * 60 + em
    duration = total_end - total_start
    hours = duration // 60
    minutes = duration % 60
    print(f"{hours}H {minutes}M")
