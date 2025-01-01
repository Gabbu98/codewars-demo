# You have been employed by the Japanese government to write a function that tests whether or not a building is strong enough to withstand a simulated earthquake.

# A building will fall if the magnitude of the earthquake is greater than the strength of the building.

# An earthquake takes the form of a 2D-Array. Each element within the Outer-Array represents a shockwave, and each element within the Inner-Arrays represents a tremor. The magnitude of the earthquake is determined by the product of the values of its shockwaves. A shockwave is equal to the sum of the values of its tremors.

# Example earthquake --> [[5,3,7],[3,3,1],[4,1,2]] ((5+3+7) * (3+3+1) * (4+1+2)) = 735

# A building begins with a strength value of 1000 when first built, but this value is subject to exponential decay of 1% per year. For more info on exponential decay, follow this link - https://en.wikipedia.org/wiki/Exponential_decay

# Given an earthquake and the age of a building, write a function that returns "Safe!" if the building is strong enough, or "Needs Reinforcement!" if it falls.

# My Solution

import math
# a func that tests whether a buidling can withstand an earthquake
# cond: if mag > strenght of building => falls
# input: 2d array; outer=shockwave, inner=tremor
# magnitude=product of shockwaves (outer) and shockwave=sum of tremor (inner)

# building strength starts at 1000 with exp decay of 1% per year

# returns "Safe" or "Needs Reinforcement"
def strong_enough(earthquake, age):
    magnitude = 1
    for n in earthquake:
        sum = 0
        for m in n:
            sum=sum+m
        magnitude = magnitude * sum
        
    strength = 1000 * math.pow(0.99,age)
    # your code here
    return "Needs Reinforcement!" if magnitude > strength else "Safe!"