x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
print("________________________")
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
print("________________________")
