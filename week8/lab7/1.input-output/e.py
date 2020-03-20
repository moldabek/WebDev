n = int(input())
m = int(input())

a = (n * m)% 109

b = (a + 109) % 109 + 1

print(b)