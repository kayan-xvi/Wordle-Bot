#----------------------------
'''
def letterpopularity():
    with open('data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            n = 0
            for number in row:
                lettercount[n] = number
                n+= 1
    if lettercount[25] == 0:
        with open('large.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                for word in row:
                    wordlist.append(word)
                    for letter in word:
                        if (ord(letter) - 97) >= 0 and (ord(letter) - 97) <= 25:
                            lettercount[ord(letter) - 97] += 1
        with open('data.csv', 'w', newline='') as file:
            reader = csv.writer(file)
            reader.writerow(lettercount)

#----------------------------

def storewords():
    if not wordlist:
        with open('large.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                for word in row:
                    wordlist.append(word)
                    if len(word) == 5:
                        fivewordlist.append(word)

#----------------------------

letterpopularity()
storewords()
print(fiveletterlist)
'''
#----------------------------

def wordsss(): 
    import csv 
    with open('large.csv', newline='') as csvfile: 
        reader = csv.reader(csvfile)
        wordlist = []
        for row in reader: 
            for number in row: 
                print(number)
                wordlist.append(word)
    return wordlist
print(wordsss())

#----------------------------
'''
def getwords():
    ''
    Getting list of 5 letter words from website 
    No argument
    Return = string of all words from link
    ''
    from urllib.request import urlopen
    url = "https://gist.githubusercontent.com/cfreshman/cdcdf777450c5b5301e439061d29694c/raw/de1df631b45492e0974f7affe266ec36fed736eb/wordle-allowed-guesses.txt"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html
'''
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
# TEST
    #print('\n REPEAT LET')
    #print('len possible: {}'.format(len(possible)))
    #print('len _possible: {}'.format(len(_possible)))
    
    for i in range(len(possible)-1, -1, -1): 
        if any(possible[i].count(x) > 1 for x in possible[i]):
            possible.remove(possible[i])
    
# TEST
    #print('len possible: {}'.format(len(possible)))
    #print('len _possible: {}'.format(len(_possible)))
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

def remove(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible, result): 
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
    
    print('_not is {}'.format(_not))
    
    for i in range(1,6): 
        # i is the number of position _not being referred to 
        for j in range(len(_not[i])):
            # j is the number in that of yellows in position 
            for k in range(len(_possible)-1,-1,-1):
                # k is the number iterating through _possible
                if _not[i][j] == _possible[k][i-1]:
                    #print('{} == {}'.format(_not[i][j], _possible[k][i-1]))
                    #print('{} has been removed'.format(_possible[j]))
                    #print('{} is being removed from _possible'.format(_possible[k]))
                    _possible.remove(_possible[k])
                    
    '''
    lse: 
    print(str(_possible) + 'has not been removed')
    '''
    #_black.clear()
    #print('\n This is _blacks once it has been cleared')
    #print(_black)
    
    return _possible

#----------------------------

def feedback(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible, result):

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
            #_not[i+1].append(_attempt[_round][i])
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
    
    return _green, _yellow, _black, _answer, result
    
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
    
# TEST
    print('_attempt = {}'.format(_attempt))
    
    print('\n After singled')
    print('len possible: {}'.format(len(possible)))
    print('len _possible: {}'.format(len(_possible)))
# TEST
    #print('\n This is the current list of attempt:\n{}'.format(attempt))
    print('\n This is the word which you should use:\n{}'.format(_attempt[_round]))
    #print('Attempt = {}'.format(_attempt))
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
    
# TEST
    print('\n After specific place removal')
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

def new(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible, result):
    '''
    This is the function for the whole process of a new round
    Arguments = list of all possible words, list of green letters, list of yellow letters, list of green letters, round number
    '''
    
    if _round >= 0:    
        print('_attempt[_round] = []'.format(_attempt[_round]))
        _possible.remove(_attempt[_round])
    _round += 1
    
    print('\n After last guess removed')
    print('len possible: {}'.format(len(possible)))
    print('len _possible: {}'.format(len(_possible)))
    
    _possible = remove(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible, result)
    transferlist(_possible, possible)
    
    print('\n After rmeoved and list tranferred')
    print('len possible: {}'.format(len(possible)))
    print('len _possible: {}'.format(len(_possible)))

# TEST
    print('\n This is when either explore or complete are run')
    newpossible = ''
    # This is what happens if more than 2 letters are g/y or small _possible
    if len(_green) + len(_yellow) > 2 or len(_possible) < 100: 
        print('\n After complete chosen')
        print('len possible: {}'.format(len(possible)))
        print('len _possible: {}'.format(len(_possible)))
        _attempt, _possible = complete(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible)
    
    # This is what happens if 2 or more letters are g/y
    
    else:
        print('\n After explore chosen')
        print('len possible: {}'.format(len(possible)))
        print('len _possible: {}'.format(len(_possible)))
        _attempt, _possible = explore(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible)
    
    return _attempt, _possible, _round
    
#----------------------------#
#----MAIN EXECUTION BLOCK----#
#----------------------------#

_words = getwords()
_wordlist = _words.split('\n')

notincl = ['aeros', 'soare', 'aesir', 'aulos', 'inula', 'hutia', 'knowe', 'tride', 'agoge', 'amove', 'plook', 'cloff', 'cloop', 'plouk', 'sasse', 'sease', 'easle', 'salle', 'salse', 'mease', 'muirs', 'shirs']
incl = ['vivid', 'arose', 'pride','bride', 'abode', 'awoke', 'flock', 'stake', 'stale', 'stage', 'stave']
for i in range(len(notincl)): 
    _wordlist.remove(notincl[i])
for i in range(len(incl)):
    _wordlist.append(incl[i])
    
_round = -1
_green = []
_yellow = []
_black = []
_answer = {1:'?', 2:'?', 3:'?', 4:'?', 5:'?'}
_not = {1:[], 2:[], 3:[], 4:[], 5:[]}
_attempt = []
result = ''
attempt = ''

_possible = []
transferlist(_wordlist,_possible)
possible0 = []

# TEST
#print('len {} and {}'. format(len(_possible), len(possible0)))

_attempt, _possible, _round = new(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible0, result)

# TEST
#print ('_attempt = {}, len(_possible) = {}'.format(_attempt, len(_possible)))

_green, _yellow, _black, _answer, result = feedback(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible0, result)

# TEST
print('_attempt after feedback() = {}'.format(_attempt))
print('_green, _yellow, _black, _answer = {},{},{},{}'.format(_green, _yellow, _black, _answer))

# TEST-
print('\n Before round 2 ')
print('len possible0: {}'.format(len(possible0)))
print('len _possible: {}'.format(len(_possible)))

possible1 = []
_attempt, _possible, _round = new(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible1, result)

# TEST
print('len(_POSSIBLE) = {}'.format(len(_possible)))

_green, _yellow, _black, _answer, result = feedback(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible1, result)

possible2 = []
_attempt, _possible, _round = new(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible2, result)
_green, _yellow, _black, _answer, result = feedback(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible2, result)

possible3 = []
_attempt, _possible, _round = new(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible3, result)
_green, _yellow, _black, _answer, result = feedback(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible3, result)

possible4 = []
_attempt, _possible, _round = new(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible4, result)
_green, _yellow, _black, _answer, result = feedback(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible4, result)

possible5 = []
_attempt, _possible, _round = new(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible5, result)
_green, _yellow, _black, _answer, result = feedback(_round, _green, _yellow, _black, _answer, _not, _attempt, _possible, possible5, result)













