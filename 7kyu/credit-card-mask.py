# Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

# Your task is to write a function maskify, which changes all but the last four characters into '#'.

# Examples (input --> output):
# "4556364607935616" --> "############5616"
#      "64607935616" -->      "#######5616"
#                "1" -->                "1"
#                 "" -->                 ""

# // "What was the name of your first pet?"
# "Skippy" --> "##ippy"
# "Nananananananananananananananana Batman!" --> "####################################man!"

# Ny Solution
# return masked string
def maskify(cc):
    result = ""
    # change the input to a string
    input = str(cc)
    
    # get size of string
    # size -4 and check if negative
    remainingSize = len(input) - 4
    
    # if negative dont do anything else iterate for remaining size
    if remainingSize > 0:
        i = 0
        
        while(i < len(input)):
            if i < remainingSize:
                result += "#"  # mask with #
            else:
                result += input[i]  # add actual character
            i = i + 1
        
        return result
    else:
        return input