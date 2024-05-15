#   using temp
def ratateArray(nums,pos):
    temp=nums[pos:]
    return temp+nums[:pos]
nums=[1,2,3,4,5,6,7]
d = 2
print(ratateArray(nums,d))

# rotating one by one
def ratateArray(nums,pos):
    p=1
    while(p<=pos):
        temp=nums[0]
        for i in range(len(nums)-1):
            nums[i]=nums[i+1]
        nums[len(nums)-1]=(temp)
        p+=1
    return nums
nums=[1,2,3,4,5,6,7]
d = 2
print(ratateArray(nums,d))