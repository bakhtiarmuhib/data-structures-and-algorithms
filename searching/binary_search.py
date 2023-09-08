import math
def binary_search(elements: list, findingValue):
    left, right = 0,len(elements)-1
    
    while not (left >= right):
        mid = math.floor((left + right)/2)
        if findingValue == elements[mid]:
            return elements[mid]
        elif(findingValue > elements[mid]):
            left = mid + 1
        elif findingValue < elements[mid]:
            right = mid -1
    return "Element not found"



print(binary_search([5,7,9,10,11,12,13,14],1))


# mid formula: mid = floor((left+right)/2)
# loop breaking condition : left >= right

#algorithm logic: finding value == elements[mid] -> return mid
#                 finding value > elements[mid]  -> left = mid + 1
#                 finding value < elements[mid]  -> right = mid - 1


# time complexity:
# best case : O(1)
# worst case : O(log(n))
# average case : O(log(n))

# memory complexity:O(n)