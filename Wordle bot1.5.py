
def getwords():
    '''
    Getting list of 5 letter words from website 
    No argument
    Return = string of all words from link
    '''
    from urllib.request import urlopen
    url = "https://gist.githubusercontent.com/cfreshman/cdcdf777450c5b5301e439061d29694c/raw/de1df631b45492e0974f7affe266ec36fed736eb/wordle-allowed-guesses.txt"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html

#----------------------------

def counting(_words):
    '''
    Function to count the number of occurances of each letter in the alphabet
    Argument = string of all words from link 
    Return = dictionary of all letter occurance 
    '''
    letterlist = {}
    alphabet = 'abcdefghijklmonpqrstuvwxyz'
    for letter in alphabet: 
        letterlist[letter] = _words.count(letter)
    return letterlist

#----------------------------

def transferlist(original, new): 
    '''
    This function is for transferring information from one list into another list which can be used separately 
    Argument = list of original variable, new one being created
    Return = new list being copied 
    '''
    for i in range(len(original)):
        new.append(original[i])
    return new
    
#----------------------------

def ordering(letterlist):
    '''
    Ordering the letters from least to most occurances 
    Argument = dicitionary of all letter occurances 
    Output = list of letter occurances in ascending order 
    '''
    order = []
    for i in range(26):
        least = 10000
        saved = ''
        for letter,number in letterlist.items():
            if number < least: 
                least = number
                saved = letter
        letterlist[saved] = 10000
        order.append(saved)
    
    return(order)

#----------------------------

def repeat_let(possible): 
    '''
    Function removes any words from possible if it contains a repeat of at least 1 letter 
    Argument = list of all words 
    Return = boolean of if the word contains a letter repeat or not 
    '''
    
    for i in range(len(possible)-1, -1, -1): 
        if any(possible[i].count(x) > 1 for x in possible[i]):
            possible.remove(possible[i])
    
#----------------------------

def single(possible, order):
    '''
    Finding list of possible words by removing words with the least common letters in order 
    Do this until only 1 word or there are only 5 letters left 
    Argument = 
    '''
    var = 0
    while len(possible) > 1 and var <= 22: 
        for length in range(len(possible)-1, -1, -1): 
            if order[var] in possible[length] and len(possible) > 1: 
                possible.remove(possible[length])
        var += 1
    
    return(possible)

#----------------------------

def feedback(_round):
    '''
    This adds each letter to _answer, _green, _yellow, _black using user input
    Arguments = round number
    Return 
    '''
    result = input('What was the result? (g = green, y = yellow, b = black) \n').lower().replace(' ','')
    
    if result == 'ggggg':
        print('Complete')
        exit()
    #_possible.remove(attempt)
    
    print('\n This is the word for round being used:')
    print(attempt)
    print(attempt[_round])
    for i in range(5): 
        if result[i] == 'g':
            _answer[i+1] = attempt[_round][i]
            _green.append(attempt[_round][i])
        if result[i] == 'y':
            _yellow.append(attempt[_round][i])
        if result[i] == 'b':
            _black.insert(0,attempt[_round][i])
    
# TEST
    print('\n This prints what we currently know about the answer:')
    print(_answer)
    print('\n These are the greens:')
    print(_green)
    print('\n These are the yellows:')
    print(_yellow)
    print('\n These are the blacks:')
    print(_black)

#----------------------------

def remove(_black, _possible): 
    '''
    Function takes any words containing any _blacks out of _possible
    Arguments = list of black letters, overall possible words 
    No return 
    '''
    for a in range(len(_black)):
        for i in range(len(_possible)-1,-1,-1):
            if _black[a] in _possible[i]:
                _possible.remove(_possible[i])
            '''
            lse: 
                print(str(_possible) + 'has not been removed')
            '''
    #_black.clear()
    print('\n This is _blacks once it has been cleared')
    print(_black)
    
    return _possible

#----------------------------

def explore(_possible, _green, _yellow, _black, _round): 
    '''
    The aim of this function is finding new letters which are in the word rather than trying to find thew actual word
    Arguments = list of all overall possible words, list of green letters, list of all yellow letters, list of all black letters, round number
    '''
# TEST
    print(len(_possible))
    
    letterlist = counting(str(_possible))
    
# TEST
    print(letterlist)
    
    repeat_let(_possible)
    order = ordering(letterlist)
    attempt.append(single(_possible, order)[0])
    
# TEST
    print('\n This is the current list of attempt:\n{}'.format(attempt))
    print('\n This is the word which you should use:\n{}'.format(attempt[_round]))


#----------------------------

def new(_possible, _green, _yellow, _black, _round):
    '''
    This is the function for the whole process of a new round
    Arguments = list of all possible words, list of green letters, list of yellow letters, list of green letters, round number
    '''
    _round += 1
    
# TEST
    print('\n This is the number of all possible words')
    print(len(_possible))
    
    _possible = remove(_black, _possible)
    
# TEST
    print('\n This is the number of all possible words after the blacks have been removed')
    print(len(_possible))
    print('\n This is the current possible list:')
    print(_possible)
    
    # This is what happens if less than 2 letters are g/y
    if len(_green) + len(_yellow) < 2: 
        explore(_possible, _green, _yellow, _black, _round)
    
    # This is what happens if 2 or more letters are g/y
    '''
    else:
        complete(_possible, _green, _yellow, _black)
    '''
    return _round
    
#----------------------------#
#----MAIN EXECUTION BLOCK----#
#----------------------------#

_round = 0
_green = []
_yellow = []
_black = []
_answer = {1:'?', 2:'?', 3:'?', 4:'?', 5:'?'}

_words = getwords()
_wordlist = _words.split('\n')
possible = _words.split('\n')
_possible = _words.split('\n')
letterlist = counting(_words)

# TEST
print('Letterlist is:')
print(letterlist)

order = []
transferlist(ordering(letterlist), order)

# TEST
print('\n Order list of letter is:')
print(order)

# TEST
print('\n The number of possible words total:')
print(len(possible))

repeat_let(possible)

# TEST
print('\n The number of possible words once ones containg letter repeats have been removed:') 
print(len(possible))

#print('\n The list of possible words once letter repeats have been removed:')
#print(possible)

single(possible,order)

# TEST
print('\n The list of possible words once singled out a single word:')
print(len(possible))

print('\n This is the word which you should use:\n{}'.format(possible[0]))

attempt = [possible[0]]
feedback(_round)

_possible1 = []
transferlist(_wordlist, _possible1)
_round = new(_possible1, _green, _yellow, _black, _round)
feedback(_round)

_possible2 = []
transferlist(_wordlist, _possible2)
_round = new(_possible2, _green, _yellow, _black, _round)
feedback(_round)

print('ROUND 3')
_possible3 = []
transferlist(_wordlist, _possible3)
_round = new(_possible3, _green, _yellow, _black, _round)















