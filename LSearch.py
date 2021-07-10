pos = -1
def LSearch(list1,key):
      for i in range(len(list1)-1):
            if list1[i]==key:
                  globals()["pos"]=i
                  return True
      return False
list1 = [88,77,66,44,23,22]
key = 77
if LSearch(list1,key):
      print("Found at",pos+1)
else:
      print("Not Found")
