# Problem
# Complete the function that takes an odd integer (0 < n < 1000000) which is the difference between two consecutive perfect squares, and return these squares as a string in the format "bigger-smaller"

# Examples
# 9  -->  "25-16"
# 5  -->  "9-4"
# 7  -->  "16-9"

# Solution

# 1,2,3,4,5 -> x
# 1,4,9,16,25 -> x^2 - (x-1)^2
# 1,3,5,7,9 -> num = roundUp(num / 2) = x
def find_squares(num):
    
    # get position
    x = (num / 2) + 0.5
    return str(round(x*x))+"-"+str(round((x-1)*(x-1)))
    
    