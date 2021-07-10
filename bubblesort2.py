def sort(nums):
      for i in range(len(nums)-1,0,-1):
            for j in range(i):
                  if nums[j]>nums[j+1]:
                        nums[j],nums[j+1]=nums[j+1],nums[j]
                  # print(nums)



nums = [66,554,222,1,11,223,3,4,5,66]
sort(nums)
print(nums)
