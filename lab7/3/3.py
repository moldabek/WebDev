from math import sqrt
n = int(input())
m = int(input())
for i in range(n,m + 1):
    if int(sqrt(i)) * int(sqrt(i)) == i:
        print(i)
