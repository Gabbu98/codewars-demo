# Given a list of integers values, your job is to return the sum of the values; however, if the same integer value appears multiple times in the list, you can only count it once in your sum.

# For example:

# [ 1, 2, 3] ==> 6

# [ 1, 3, 8, 1, 8] ==> 12

# [ -1, -1, 5, 2, -7] ==> -1

# [] ==> None

# My Solution

# iterate
# remove redundant
# sum
# 2n time
# n space at worst

# iterate
# take note and sum
# n time
# n + 1 space

# preferred
# list set 
# sum
# n time
# n space

def unique_sum(lst):
    print(lst)
    if lst==[]:
        print(lst)
        return None
    
    lst = list(set(lst))
    
    sum=0
    for n in lst:
        sum=n+sum
    print(sum)
    return sum