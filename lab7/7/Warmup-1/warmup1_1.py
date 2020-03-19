def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False


n = bool(input())
m = bool(input())

print(monkey_trouble(n,m))