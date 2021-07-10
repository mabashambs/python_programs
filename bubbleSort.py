def BubbleSort(nums):
      for i in range(len(nums)-1,0,-1):
            for j in range(i):
                  if nums[j]>nums[j+1]:
                        nums[j],nums[j+1]=nums[j+1],nums[j]

nums = []
for x in range(1,20,2):
      nums.append(x)
nums.reverse()
print(nums)
BubbleSort(nums)
print(nums)
