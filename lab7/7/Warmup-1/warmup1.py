def sleep_in(weekday, vacation):
  if weekday == False and vacation == False:
    return True
  elif weekday == True and vacation == False:
    return False
  elif weekday == False and vacation == True:
    return True
  else:
    return True


n = bool(input())
m = bool(input())

print(sleep_in(n,m))