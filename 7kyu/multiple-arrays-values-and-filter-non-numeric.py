# Your task is to write a function, which takes two arguments and returns a sequence. First argument is a sequence of values, second is multiplier. 
# The function should filter all non-numeric values and multiply the rest by given multiplier.

# My Solution
def multiply_and_filter(seq, multiplier): 
    # your code here
    
    numbersList = []
    
    for x in seq:
        if type(x) is int or type(x) is float:
            numbersList.append(float(x) * float(multiplier))
            
    
    return numbersList