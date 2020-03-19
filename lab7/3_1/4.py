from math import sqrt

n = int(input())

cnt = 2

chk = False

if n == 1:
    chk = True
else:
    while n > cnt:
        cnt *= 2
    if n == cnt:
        chk = True
if chk == True:
    print("YES")
else:
    print("NO")