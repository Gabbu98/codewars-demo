# Task
# Given an non-empty list or array (depending on language) of non-empty uppercase words, compute the minimum number of words, which, when removed from the list, leaves the rest of the list in strictly ascending lexicographic order.

# Examples:
# ["THE","QUICK","BROWN","FOX","JUMPS","OVER","THE","LAZY","DOG"] should return 4, because removing "THE", "QUICK", "LAZY" & "DOG" leaves the sorted list ["BROWN","FOX","JUMPS","OVER","THE"].

# ["JACKDAW","LOVE","MY","BIG","SPHINX","OF","QUARTZ"] should return 2, because removing "BIG" & "SPHINX" leaves the sorted list ["JACKDAW","LOVE","MY","OF","QUARTZ"].

# ["A","A","A","A"] should return 3, because equal elements are NOT regarded as sorted, so all but one of them need to be removed.

# Source: Midwest Instructional Computing Symposium 2011 http://micsymposium.org/
# Somewhat similar, but harder, kata are Make an increasing sequence and Find the Longest Increasing or Decreasing Combination in an Array

# My Solution
# lis algorithm

def sort_by_exclusion(words):
    # check if list is empty
    n = len(words)    
    
    # initialise a list all with 1s
    init = [1] * n
        
    for i in range(1,n):
        for j in range(i):
            if words[j] < words[i] and init[i] < init[j] + 1:
                init[i] = init[j]+1
    
    max_init = max(init)
    
    return n - max_init