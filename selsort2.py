def sort(nums):
      for i in range(len(nums)-1):
            mini = i
            for j in range(i,len(nums)):
                  if nums[j]< nums[mini]:
                        mini = j
            nums[i],nums[mini] = nums[mini],nums[i]
                  

nums = [88,66,54,33,22,1,0,12,22222,23]
sort(nums)
print(nums)
