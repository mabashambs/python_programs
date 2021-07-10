pos = -1
def BSearch(list1,key):
      lb=0
      ub = len(list1)-1
      while lb<=ub:
            mid = (lb+ub)//2
            if list1[mid] == key:
                  globals()['pos'] = mid
                  return True
            else:
                  if list1[mid]<key:
                        lb = mid+1
                  else:
                        ub = mid-1

      return False



list1 = [1,22,33,44,55,66,67,888] #list must be sorted in Linear Search.
key = 888
if BSearch(list1,key):
      print("found at",pos+1)
else:
      print("not found")
