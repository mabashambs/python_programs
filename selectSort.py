def SelSort(nums):
      for i in range(len(nums)-1):
            mini = i
            for j in range(i,len(nums)):
                  if nums[j]<nums[mini]:
                        mini = j
            nums[i],nums[mini]=nums[mini],nums[i]
nums=[]
for i in range(1,30,3):
      nums.append(i)
print(nums)
nums.reverse()
print(nums)
SelSort(nums)
print(nums)
