#iterative method
def reversingArray(nums):
    s=0
    e=len(nums)-1
    while s<=e:
        nums[s],nums[e]=nums[e],nums[s]
        s+=1
        e-=1
    return nums

print(reversingArray([1,2,3,4,5,6,7,8,9]))

#slicing
def reversingArray(nums):
    return nums[::-1]
print(reversingArray([1,2,3,4,5,6,7,8,9]))

#recuyousion
def reversingArray(nums,s,e):
    if s<=e:
        nums[s],nums[e]=nums[e],nums[s]
        reversingArray(nums,s+1,e-1)
    return nums

print(reversingArray([1,2,3,4,5,6,7,8,9],0,8))




