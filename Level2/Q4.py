def rotate_array(nums, k):
    if(k==0 or len(nums)<=1): return
    k = k%len(nums)
    l = 0
    r = len(nums)-1

    while(l<r):
        nums[l],nums[r] = nums[r],nums[l]
        l+=1
        r-=1

    
    l = 0
    r = k - 1

    while(l<r):
        nums[l],nums[r] = nums[r],nums[l]
        l+=1
        r-=1
    l = k
    r = len(nums)-1

    while(l<r):
        nums[l],nums[r] = nums[r],nums[l]
        l+=1
        r-=1


arr = [1, 2, 3, 4, 5]
D = 2


rotated_arr = rotate_array(arr, D)

print(f"Array after rotation: {arr}")
