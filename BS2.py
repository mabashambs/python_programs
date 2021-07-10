pos = -1
def BSearch(list1,key):
      lb = 0
      ub = len(list1)-1
      while lb <= ub:
            mid = (lb+ub)//2
            if list1[mid] == key:
                  globals()["pos"] = mid
                  return True
            else:
                  if list1[mid] < key:
                        lb = mid + 1
                  else:
                        ub = mid - 1
      return False
list1 = list(range(1,20,2))
print(list1)
key = int(input("key : "))
if BSearch(list1,key):
      print("found at",pos+1)
else:print("not found")
