thisdict = {
    "model":"Ford",
    "year":"1994"
}
x = thisdict["model"]
print(x)
print("_________________________________________________")
m = thisdict.get("model")
print(m)
print("_________________________________________________")
for x in thisdict:
  print(x)
  print("_________________________________________________")
  for x in thisdict.values():
      print(x)
      print("_________________________________________________")
      for x, y in thisdict.items():
          print(x, y)