def bubbleSort(nums : list[int]):
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] =  nums[j+1]
                nums[j+1] = temp
    return nums


print(bubbleSort([8,4,9,2,1]))


# time complexity = O(n**2)
# memory complexity = O(1)

