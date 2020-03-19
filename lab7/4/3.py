n = int(input())

a = [int(i) for i in input().split()]

l = [i for i in a if i > 0]

print(len(l))	