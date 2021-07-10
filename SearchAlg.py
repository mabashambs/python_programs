listVals = list(eval(input("Enter a list of Vals : ")))
print(listVals)
Key = eval(input("Enter Key Element to search : "))
if Key in listVals:
      print("true")
      print(Key.index())
else:
      print("false")
