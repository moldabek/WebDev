n = int(input())
m = int(input())
a = int(input())
b = int(input())

for i in range(n,m + 1):
    if i % b == a:
        print(i, end = " ")
