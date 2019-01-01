thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
print(len(thislist))
thislist.append("orange")
for x in thislist:
  print(x)
  print("_________________________________________")
  i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

print("____________________________________________")
for x in "banana":
  print(x)

print("____________________________________________")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

print("____________________________________________")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    print(x+"ananab")
    continue
  print(x)
print("____________________________________________")
def my_function():
  print("Hello from a function")

my_function()
