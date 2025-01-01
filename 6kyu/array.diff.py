# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list b keeping their order.

# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:

# array_diff([1,2,2,2,3],[2]) == [1,3]

# My Solution

# Goal: subtracts a list from another and returns a result
# remove all values from list a which are present in b keeping order
# Example [1,2]-[1] = [2], [1,2,2,3]-[2]=[1,3]

# solution 1:
# iterating,check and remove
# time complexity: n squared
# space complexity: 1

# solution 2:
# iterating, contains and remove
# time complexity: n
# space complexity: 1

def array_diff(a, b):
    c = []
    for number in a:
        if number not in b:
            c.append(number)
    return c