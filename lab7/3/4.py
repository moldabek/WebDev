from math import sqrt
n = int(input())
l = []
for i in range(2,n):
    if n % i == 0:
        l.append(i)
    
if len(l) > 0:
    print(l[0])
else:
    print(n)
