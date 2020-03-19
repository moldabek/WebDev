n = int(input())

l = []

while n != 0:
        l.append(n)
        n = n - 1

l.sort()

for i in range(len(l)):
    print(i + 1, end='')
    
               