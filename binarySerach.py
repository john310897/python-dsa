def bs(nums,key):
    l=0
    r=len(nums)
    while(l<=r):
        m=l+(r-l)//2
        if(key==nums[m]):
            return m
        elif(key>nums[m]):
            l=m+1
        else:
            r=m-1
r=bs([1,2,3,4,5,6],3)
print(r)