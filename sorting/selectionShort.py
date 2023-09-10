def selectionSort(nums : list):
    for i in range((len(nums))):
        indexNumber =  i
        for j in range(i+1,(len(nums))):
            if nums[indexNumber] > nums[j]:
                indexNumber = j
        if indexNumber != i :
            temp = nums[i]
            nums[i]=nums[indexNumber]
            nums[indexNumber]=temp
    return nums


print(selectionSort([4,8,2,1]))

# time complexity O(n**2)
# memory complexity : O(1)