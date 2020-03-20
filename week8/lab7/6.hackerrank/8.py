import string
lower = string.ascii_lowercase
upper = string.ascii_uppercase 
def swap_case(s):
    t = []
    for i in range(len(s)):
        if s[i] in lower:
            t.append(s[i].upper())
        elif s[i] in upper:
            t.append(s[i].lower())
        else:
            t.append(s[i])
    return ''.join(t)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)