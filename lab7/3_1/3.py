n = int(input())
two_in_power = 1
power = 1
while two_in_power <= n:
    two_in_power *= 2
    power += 1
    print(two_in_power // 2, end = " ")
