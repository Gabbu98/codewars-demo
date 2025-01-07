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




pointer=0

class Bracket:
    def __init__(self, open_bracket_index, close_bracket_index, value):
        self.open_bracket_index=open_bracket_index
        self.close_bracket_index=close_bracket_index
        self.value=value
        
    def __repr__(self):
        return f"Bracket(open_bracket_index='{self.open_bracket_index}',close_bracket_index='{self.close_bracket_index}',value='{self.value}')"

class Element:
    def __init__(self,key,value):
        self.key=key
        self.value=value

def tokenize_brackets(elements):
    brackets=[]
    n=len(elements)
    open_brackets_stack=[]
    closing_brackets_queue=[]
    prev=""
    for i in range(n):
        characters = elements[i].split('-')
        if characters[0]=='(' or characters[0]=='{' or characters[0]=='[':
            open_brackets_stack.append(i)
            prev=characters[0]
        if characters[0]==')' or characters[0]=='}' or characters[0]==']':
            if prev=='(' or prev=='[' or prev=='{':
                open_bracket = open_brackets_stack.pop()
                if len(characters) > 1:
                    bracket = Bracket(open_bracket,i,int(characters[1]))
                    brackets.append(bracket)
                else:
                    bracket = Bracket(open_bracket,i,1)
                    brackets.append(bracket)
                prev=""
                continue
            if len(characters) > 1: 
                closing_brackets_queue.append(str(i)+"-"+characters[1])
            else:
                closing_brackets_queue.append(str(i)+"-"+str(1))
                
    n=len(closing_brackets_queue)
    for i in range(n):
        cls_chars = closing_brackets_queue.pop(0).split('-')
        open_bracket = open_brackets_stack.pop()
        bracket = Bracket(open_bracket,int(cls_chars[0]),int(cls_chars[1]))
        brackets.append(bracket)
        
    print(brackets)
    return brackets
        
def count_brackets(elements):
    open_brackets=[]
    n = len(elements)
    brackets=[]
    # iterate
    for i in range(n):
        characters = elements[i].split('-')
        if characters[0]=='(' or characters[0]=='{' or characters[0]=='[':
            open_brackets.append(i)
        if characters[0]==')' or characters[0]=='}' or characters[0]==']':
            if len(characters) > 1: 
                brackets.append(Bracket(characters[0], characters[1], open_brackets.pop()))
            else: 
                brackets.append(Bracket(characters[0], '1', open_brackets.pop()))
    
    return brackets
        
def counter(elements, brackets):
    n = len(elements)
    elements_dict = {}
    multiplier=1
    prev_mutliplier_stack=[Bracket(1000,1000,1)]
    brackets.append(Bracket(1000,1000,1))
    for i in range(n):
        characters = elements[i].split('-')
        character = characters[0]
        value=1
        closing_brackets=[']','}',')']
        opening_brackets=['[','{','(']
        
        if character=='{' or character=='(' or character=='[':
            for j in range(len(brackets)):
                if i == brackets[j].open_bracket_index:
                    prev_mutliplier_stack.append(brackets[j])
                    multi = 1
                    for k in range(len(prev_mutliplier_stack)):
                        multi = multi * prev_mutliplier_stack[k].value
                    multiplier = multi
                    continue
                    
            
        if character==')' or character=='}' or character==']':
            prev_mutliplier_stack.pop()
            multiplier = brackets[-1].value
            
            
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
    brackets = tokenize_brackets(elements)
    return counter(elements,brackets)
    
    pass
    