# You are on a party with your friends and one of them suggest to play a game called "Magic Music Box". The game consists of a magic music box that is playing one by one all the music notes in order from DO to SI over and over.
# The goal of the game is to store in the magic music box words that contain the musical note that is being played at each moment.

# Task
# In this kata you have to create a function that given an array of words returns another array with all the words that have been stored in the magic music box in the correct order.
# A word can be stored in the magic music box when it contains the musical note that the box is playing at each moment. When a word is stored, the music box starts to play the next note, and so on.
# The function must try to store every word from the input if possible, even if it means to retry some words that didn't fitted previuosly.
# If there are no more words in the input that can be stored in the box, the function should stop and return the array with the stored words in the order they have been stored.

# Rules
# The same word cannot be stored more than once.
# The magic music box plays the musical notes over and over, in a cyclic infinite loop.
# If a word cannot be stored, it does not mean it could not be stored in the future with the appropiate note.
# You don't have to verify the word, you only have to check that it contains the musical note with all its letters together (i.e. SOLAR would be a valid word but SOCIAL wouldn't).
# The musical notes are represented in the european solfège format (DO, RE, MI, FA, SOL, LA, SI).
# The method must return an empty array if there are no words present inside the array.

# Example
# Given the input array ["DOWN","PLANE","AMIDST","REPTILE","SOFA","SOLAR","SILENCE","DOWN","MARKDOWN"]
# The function flow should be:
# As the first musical note is DO, the word DOWN fits, and is stored inside the box.
# The next note is RE, and iterating the array, the next word that fits is REPTILE.
# The next note is MI, but if we continue in the array, we don't find any word that fits, so we should try again from the begining. This time, we find AMIDST, which fits.
# The flow continues like this for the next musical notes (FA, SOL, LA, SI). At this point, our temporal resulted array looks like this: ["DOWN", "REPTILE", "AMIDST", "SOFA", "SOLAR", "PLANE", "SILENCE"]
# The next note is DO again, because the music box never stops playing notes. Following the array, we find the word DOWN. The word itself fits with the note, but as long as it is forbidden to repeat words, we have to omit it. The next word that fits is MARKDOWN, we store it and continue.
# The next note is RE, but this time, searching a fitting word, we end doing a complete iteration over the array with finding any, so the function ends and return the definitive array solution: ["DOWN","REPTILE","AMIDST","SOFA","SOLAR","PLANE","SILENCE","MARKDOWN"]

# Magic Music Box -> returns an array of words stored in it in a correct order
# If word contains musical note -> store
# Rules
    # same word cannot be stored more than once
    # magic music box plays the musical over and over in a cyclic infinite loop
    # just make sure the note exists in the word
    # MUSICAL NOTES = DO, RE, MI, FA, SOL, LA, SI
    # no words = return empty array
class Word_Counter:
    def __init__(self, counter, musical_notes):
        self.counter = counter
        self.musical_notes = musical_notes
        
    def reevaluate(self):
        if self.counter>0:
            self.counter = self.counter - len(self.musical_notes)
        
    def __repr__(self):
        return f"Word_Counter(counter='{self.counter}',musical_notes='{self.musical_notes}')"

def evaluate(words_dict):
    sum = 0

    for val in words_dict.values():
        sum += val.counter  # Add the counter value of each value to the sum
    if sum == 0:
        return True

    return False

def update_dict(hasMatched,word,words_dict,m,musical_notes,i):
    word_from_dict = words_dict.get(word)
    word_from_dict.counter = m
    
    if hasMatched and musical_notes[i] not in word_from_dict.musical_notes:
        word_from_dict.musical_notes = musical_notes
        
    if not hasMatched and musical_notes[i] not in word_from_dict.musical_notes:
        word_from_dict.musical_notes.append(musical_notes[i])

    word_from_dict.reevaluate()
    words_dict[word] = word_from_dict
    return words_dict

def magic_music_box(words):
    musical_notes = ["DO", "RE", "MI", "FA", "SOL", "LA", "SI"]
    m = len(musical_notes)

    words_dict = {}
    shouldNext = False
    music_box = []
    i = 0
    j = 0
    counter = 0
    complete = False
    
    for word in words:
        words_dict[word] =  Word_Counter(m,[])
    
    while True:
        if evaluate(words_dict)==True:
            break
            
        if counter == len(words):
            break
        
        if shouldNext:
            i = i+1
            if i == m:
                i = 0
            shouldNext = False
            counter = 0
            
        if musical_notes[i] in words[j] and words[j] not in music_box:
            music_box.append(words[j])
            
            words_dict = update_dict(True,words[j],words_dict,m,musical_notes,i)
            
            shouldNext = True
            counter = 0
            
        else:
            words_dict = update_dict(False,words[j],words_dict,m,musical_notes,i)
            shouldNext = False
            counter += 1 

        
        j = j+1
        if j == len(words): j = 0
            
    return music_box
