def linear_search(elements : list,findingValue:int):
    index = -1
    for i in elements:
        index +=1
        if i == findingValue:
            return f"Elements {i} in index {index}"
    return "Elements not found"
    
print(linear_search([10,20,1,2,3,4,5],98))



# time complexity

# best case = O(1)
# worst case = O(n)

# average case = (summation of all case) / number of case

# average case = (1+2+3+4+5......+n) / n
#              = ((n*(n+1))/2)/n
#              = (n+1)/2
#              =O((n+1)/2)

#space complexity
# O(n)

