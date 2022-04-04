_round = -1
_green = []
_yellow = []
_black = []
_answer = {1:'?', 2:'?', 3:'?', 4:'?', 5:'?'}
_not = {1:[], 2:[], 3:[], 4:[], 5:[]}
_attempt = []

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

_words = getwords()
_wordlist = _words.split('\n')

notincl = ['aeros', 'soare', 'aesir', 'aulos', 'inula', 'hutia', 'knowe', 'tride', 'agoge', 'amove']
incl = ['vivid', 'arose', 'pride','bride', 'abode', 'awoke']
for i in range(len(notincl)): 
    _wordlist.remove(notincl[i])
for i in range(len(incl)):
    _wordlist.append(incl[i])
    
_possible = []
transferlist(_wordlist,_possible)

#----------------------------

def counting(words):
    '''
    Function to count the number of occurances of each letter in the alphabet
    Argument = string of all words from link 
    Return = dictionary of all letter occurance 
    '''
    letterlist = {}
    alphabet = 'abcdefghijklmonpqrstuvwxyz'
    for letter in alphabet: 
        letterlist[letter] = words.count(letter)
    return letterlist

#----------------------------

def transferdic(original, new): 
    '''
    This function is for transferring information from one dictionary into another list which can be used separately 
    Argument = list of original variable, new one being created
    Return = new list being copied 
    '''
    for letter, number in original.items():
        new[letter] = number
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

def repeat_let(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible): 
    '''
    Function removes any words from possible if it contains a repeat of at least 1 letter 
    Argument = (_round, _green, _yellow, black, _answer, _not, _attempt, _possible, possible)
    Return = boolean of if the word contains a letter repeat or not 
    '''
    print('\n REPEAT LET')
    print('len possible: {}'.format(len(possible)))
    print('len _possible: {}'.format(len(_possible)))
    for i in range(len(possible)-1, -1, -1): 
        if any(possible[i].count(x) > 1 for x in possible[i]):
            possible.remove(possible[i])
    print('len possible: {}'.format(len(possible)))
    print('len _possible: {}'.format(len(_possible)))
    return possible
#----------------------------

def single(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible, order):
    '''
    Finding list of possible words by removing words with the least common letters in order 
    Do this until only 1 word or there are only 5 letters left 
    Argument = (_round, _green, _yellow, black, _answer, _not, _attempt, _possible, possible)
    '''
    var = 0
    while len(possible) > 1 and var <= 22: 
        for length in range(len(possible)-1, -1, -1): 
            if order[var] in possible[length] and len(possible) > 1: 
                possible.remove(possible[length])
        var += 1
    
    return possible

#----------------------------

def feedback(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible):

    '''
    This adds each letter to _answer, _green, _yellow, _black using user input
    Arguments = (_round, _green, _yellow, black, _answer, _not, _attempt, _possible, possible)
    Return 
    '''
    result = input('What was the result? (g = green, y = yellow, b = black) \n').lower().replace(' ','')
    
    if result == 'ggggg':
        print('Complete')
        exit()
        
    for i in range(5): 
        if result[i] == 'g':
            _answer[i+1] = _attempt[_round][i]
            if not _attempt[_round][i] in _green:
                _green.append(_attempt[_round][i])
                if _attempt[_round][i] in _yellow:
                    _yellow.remove(_attempt[_round][i])
        if result[i] == 'y':
            _not[i+1].append(_attempt[_round][i])
            if not _attempt[_round][i] in _yellow:
                _yellow.append(_attempt[_round][i])
        if result[i] == 'b':
            _not[i+1].append(_attempt[_round][i])
            if not _attempt[_round][i] in _black:
                _black.insert(0,_attempt[_round][i])
    
# TEST
    print('\n This prints what we currently know about the answer:')
    print(_answer)
    print('\n This prints what we currently know about the not:')
    print(_not)
    print('\n These are the greens:')
    print(_green)
    print('\n These are the yellows:')
    print(_yellow)
    print('\n These are the blacks:')
    print(_black)
    
    return _green, _yellow, _black, _answer
    
#----------------------------

def remove(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible): 
    '''
    Function takes any words containing any _blacks out of _possible
    Arguments = (_round, _green, _yellow, black, _answer, _not, _attempt, _possible, possible)
    No return 
    '''
    for a in range(len(_black)):
        for i in range(len(_possible)-1,-1,-1):
            if _black[a] in _possible[i]: 
                if not _black[a] in _green and not _black[a] in _yellow:
                    _possible.remove(_possible[i])
            '''
            lse: 
                print(str(_possible) + 'has not been removed')
            '''
    #_black.clear()
    #print('\n This is _blacks once it has been cleared')
    #print(_black)
    
    return _possible

#----------------------------

def explore(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible): 
    '''
    The aim of this function is finding new letters which are in the word rather than trying to find the actual word
    Arguments = list of all overall possible words, list of green letters, list of all yellow letters, list of all black letters, round number
    '''
# TEST
    print('\n Explore is run')

# TEST
    print('len possible: {}'.format(len(possible)))
    print('len _possible: {}'.format(len(_possible)))
    possible = repeat_let(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible)
    
# TEST
    print('\n After repeats removed')
    print('len possible: {}'.format(len(possible)))
    print('len _possible: {}'.format(len(_possible)))
# TEST
    #print('\n This is the newest set of _possible:')
    #print(_possible)

    letterlist = counting(str(possible))
    for green in _green: 
        letterlist[green] = 0

# TEST
    print('\n This is the letterlist in explore:')
    print(letterlist)

    order = ordering(letterlist)
    
# TEST
    print('\n This is the order in explore:')
    print(order)
    
    #print('\n This is the list of possible')
    #print(_possible)
    
    singled = single(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible, order)
    _attempt.append(singled[0])
    print('_attempt = {}'.format(_attempt))
    
    print('\n After singled')
    print('len possible: {}'.format(len(possible)))
    print('len _possible: {}'.format(len(_possible)))
# TEST
    #print('\n This is the current list of attempt:\n{}'.format(attempt))
    print('\n This is the word which you should use:\n{}'.format(_attempt[_round]))
    print('Attempt = {}'.format(_attempt))
    return _attempt, _possible

#----------------------------

def complete(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible): 
    '''
    The aim of this function is finding the actual word
    Arguments = (_round, _green, _yellow, black, _answer, _not, _attempt, _possible, possible)
    '''
# TEST
    print('\n Complete is run')
    print('len possible: {}'.format(len(possible)))
    print('len _possible: {}'.format(len(_possible)))
    for i in range(1,6): 
        
        if _answer[i] != '?': 
            #print('\n _answer[{}] = {}'.format(i,_answer[i]))
            for j in range(len(_possible)-1,-1,-1): 
                #print('\n _possible[{}][{}] = {}'.format(j,i-1,_possible[j][i-1]))
                if _answer[i] != _possible[j][i-1]:
                    #print('{} has been removed'.format(_possible[j]))
                    _possible.remove(_possible[j])
    for i in range(len(_yellow)):
        for j in range(len(_possible)-1,-1,-1): 
                #print('\n _possible[{}][{}] = {}'.format(j,i-1,_possible[j][i-1]))
                if not _yellow[i] in _possible[j]:
                    #print('{} has been removed'.format(_possible[j]))
                    _possible.remove(_possible[j])
    
# TEST
    print('\n After specific place removal ')
    print('len possible: {}'.format(len(possible)))
    print('len _possible: {}'.format(len(_possible)))
    print('_possible: {}'.format(_possible))
    
    letterlist = counting(str(_possible))
    
    transferlist(_possible, possible)
    
    print('\n This is the newest letterlist: \n{}'.format(letterlist))
    order = ordering(letterlist)
    print('\n This is the newest order: \n{}'.format(order))
    print(single(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible, order))
    _attempt.append(single(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible, order)[0])
    
    print('Round = {}'.format(_round))
    print('\n This is the current list of attempt:\n{}'.format(_attempt))
    print('Round = {}'. format(_round))
    print('\n This is the word which you should use:\n{}'.format(_attempt[_round]))
    
    return _attempt, _possible
    
#----------------------------

def new(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible):
    '''
    This is the function for the whole process of a new round
    Arguments = list of all possible words, list of green letters, list of yellow letters, list of green letters, round number
    '''
    if _round >= 0:    
        _possible.remove(_attempt[_round])
    _round += 1
    _possible = remove(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible)

# TEST
    print('\n This is when either explore or complete are run')
    newpossible = ''
    # This is what happens if more than 2 letters are g/y or small _possible
    if len(_green) + len(_yellow) > 1 or len(_possible) < 100: 
        _attempt, _possible = complete(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible)
    
    # This is what happens if 2 or more letters are g/y
    
    else:
        _attempt, _possible = explore(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible)
    
    return _attempt, _possible, _round
    
#----------------------------#
#----MAIN EXECUTION BLOCK----#
#----------------------------#




'''
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
print(len(_possible))

repeat_let(_possible)

# TEST
print('\n The number of possible words once ones containg letter repeats have been removed:') 
print(len(_possible))

single(_possible,order)

# TEST
print('\n The list of possible words once singled out a single word:')
print(len(_possible))

print('\n This is the word which you should use:\n{}'.format(_possible[0]))
'''

possible0 = []
transferlist(_possible, possible0)
print('len {} and {}'. format(len(_possible), len(possible0)))
_attempt, _possible, _round = new(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible0)
print ('_attempt = {}, len(_possible) = {}'.format(_attempt, len(_possible)))
_green, _yellow, _black, _answer = feedback(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible0)
print('_green, _yellow, _black, _answer = {},{},{},{}'.format(_green, _yellow, _black, _answer))

print('len(_POSSIBLE) = {}'.format(len(_possible)))
possible1 = []
transferlist(_possible, possible1)
_attempt, _possible, _round = new(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible1)
print('len(_POSSIBLE) = {}'.format(len(_possible)))
_green, _yellow, _black, _answer = feedback(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible1)

possible2 = []
transferlist(_possible, possible2)
_attempt, _possible, _round = new(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible2)
_green, _yellow, _black, _answer = feedback(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible2)

possible3 = []
transferlist(_possible, possible3)
_attempt, _possible, _round = new(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible3)
_green, _yellow, _black, _answer = feedback(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible3)

possible4 = []
transferlist(_possible, possible4)
_attempt, _possible, _round = new(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible4)
_green, _yellow, _black, _answer = feedback(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible4)













