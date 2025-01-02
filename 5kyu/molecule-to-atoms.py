# For a given chemical formula represented by a string, count the number of atoms of each element contained in the molecule and return an object (associative array in PHP, Dictionary<string, int> in C#, Map<String,Integer> in Java).

# For example:

# water = 'H2O'
# parse_molecule(water)                 # return {H: 2, O: 1}

# magnesium_hydroxide = 'Mg(OH)2'
# parse_molecule(magnesium_hydroxide)   # return {Mg: 1, O: 2, H: 2}

# var fremy_salt = 'K4[ON(SO3)2]2'
# parse_molecule(fremySalt)             # return {K: 4, O: 14, N: 2, S: 4}
# As you can see, some formulas have brackets in them. The index outside the brackets tells you that you have to multiply count of each atom inside the bracket on this index. For example, in Fe(NO3)2 you have one iron atom, two nitrogen atoms and six oxygen atoms.

# Note that brackets may be round, square or curly and can also be nested. Index after the braces is optional.

# My Solution
class Bracket:
    def __init__(self, key, value):
        self.key=key
        self.value=value
        
    def __repr__(self):
        return f"Bracket(key='{self.key}',value='{self.value}')"

class Element:
    def __init__(self,key,value):
        self.key=key
        self.value=value

def count_brackets(elements):
    
    n = len(elements)
    brackets=[]
    # iterate
    for i in range(n):
        characters = elements[i].split('-')
        if characters[0]==')' or characters[0]=='}' or characters[0]==']':
            if len(characters) > 1: 
                brackets.append(Bracket(characters[0], characters[1]))
            else: 
                brackets.append(Bracket(characters[0], '1'))
    
    return brackets
        
def counter(elements, brackets):
    pointer=0
    n = len(elements)
    elements_dict = {}
    multiplier=1
    brackets.insert(0,Bracket('[',1))
    for i in range(n):
        characters = elements[i].split('-')
        character = characters[0]
        value=1
        closing_brackets=[']','}',')']
        opening_brackets=['[','{','(']
        print(character)
        if character=='{' or character=='(' or character=='[':
            pointer = pointer + 1
            multiplier = int(brackets[pointer].value)
            
        if character==')' or character=='}' or character==']':
            pointer = pointer - 1
            multiplier = int(brackets[pointer].value)
            
            
        if character not in closing_brackets and character not in opening_brackets and len(characters)>1:
            value = int(characters[1])
            
        if character not in closing_brackets and character not in opening_brackets:
            if character in elements_dict: 
                elements_dict[character] += value*multiplier 
            else: 
                elements_dict[character] = value*multiplier 

    return elements_dict

def parse(formula):
    n = len(formula)
    els=[]
    char=""
    element=""
    num=""
    for i in range(n):
        if formula[i].isalpha() and formula[i].isupper():
            num=""
            char=""
            char=formula[i]
            element=char
            els.append(element)
        if formula[i].isalpha() and formula[i].islower():
            element = char+formula[i]
            els.pop()
            els.append(element)
        if formula[i].isnumeric():
            num = num+formula[i]
            element = char+"-"+num
            els.pop()
            els.append(element)
        if formula[i]=="(" or formula[i]==")" or formula[i]=="[" or formula[i]=="]" or formula[i]=="{" or formula[i]=="}":
            char=""
            num=""
            char=formula[i]
            element=char
            els.append(element)
    return els

def parse_molecule(formula):
    elements = parse(formula)
    brackets = count_brackets(elements)
    return counter(elements,brackets)
    