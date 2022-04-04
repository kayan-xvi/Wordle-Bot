def getwords():
    
    # Getting list of 5 letter words from website 

    from urllib.request import urlopen
    url = "https://gist.githubusercontent.com/cfreshman/cdcdf777450c5b5301e439061d29694c/raw/de1df631b45492e0974f7affe266ec36fed736eb/wordle-allowed-guesses.txt"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html.split("\n")
    
# Creating an identity dictionary of what letters are g/y/b/? 

identity = {}
alphabet = 'abcedfghijklmnopqrstuvwxyz'

for i in range(len(alphabet)):
    identity[alphabet[i]] = '?' 

#TEST - should print: 
# {a:?, b:?, c:?, ... }
print('Identity is full of ?:')
print(str(identity) + '\n')

words = []
letterlist = {}

# Adding the words into a list of all words (words)

print('This is a complete list of all words being used:')
#words.append('abcde')
for i in range(10): #range(len(getwords())):
    words.append(getwords()[i])
    #TEST - prints all words 
    print (words[i])

    # Adding the words into a dictionary (letterlist) {letters: number of total occurances}

    for l in range(4): 
        if words[i][l] in letterlist: 
            letterlist[words[i][l]] += 1 
        else: 
            letterlist[words[i][l]] = 1

#TEST - should print in order: 
# [XXXXX]
print('\n This is the completed letterlist full of values')
print(letterlist)

order_letters = []

# Ordering the letters according to the number of their occurances - least to most common 

letterlist2 = {}
for letter, number in letterlist.items():
    letterlist2[letter] = number

print('\n letterlist')
print(letterlist)
print('\n letterlist2')
print(letterlist2)

for times in range(26): 

    least_let = ''
    least_num = 1000000

    for letter, number in letterlist2.items(): 
        #print(number)
        #print(type(number))
        #print(least_num)
        #print(type(least_num))
        if number < least_num: 
             least_num = number
             least_let = letter
    letterlist2[least_let] = 1000000 
    #print(letterlist)
    #print(letterlist2)
        #print(letterlist2)
    order_letters.append(least_let) 
        #print(order_letters)

#TEST - should print letters in order of least common to most common: 
# [XXXXX]

print('\n letterlist2 having been used:')
print(letterlist2)

print('\n order_letters:')
print(order_letters)



# Picking the first word to choose 


# Should remove all words where there are repeats of the same letter 

possible = words
var = 0
'''
for length in range(len(possible)): 
    for i in range(4): 
        a = 1
        b +=1
        print(possible[length])
        while i + a <= 4: 
            print('i = ' + str(i))
            print('a = ' + str(a))
            print('b = ' + str(b))
            #print(b)
            
            print(possible[length][b])
            #print(a)
            print(possible[length][b+a])
            if possible[length][b] == possible[length][b+a]:
                possible.remove(possible[length])
                print('removed')
                break
            a += 1 
'''
for length in range(len(possible)):
    print(possible)
    print(possible[length])
    print(length)
    i = 0
    a = 1
    while i < 4: 
        #print('Number ' + str(i) + ' letter is ' + possible[length][i])
        #print('Number ' + str(i+a) + ' letter is ' + possible[length][i+a])
        if possible[length][i] == possible[length][i+a]:
            possible.remove(possible[length])
            print('removed')
            break
        else: 
            a += 1 
            if i + a > 4: 
                i += 1
                a = 1
                if i == 4: 
                    break
        

# Finding list of possible words by removing words with the least common letters 
# Do this until only 1 word or there are only 5 letters left 

while len(possible) > 1 and var <= 22: 
    for length in range(len(possible)): 
       if order_letters[var] in possible[length]: 
            possible.remove(possible[length])
    var += 1

# Print the word to play, or get down to the single word 
# Done by finding the word with the greatest total occurances 
# If equal it will just pick the first one of that occurance 

if len(posisble) == 1: 
    print('You should play '. format(possible[0]))
else: 
    max_occ = 0 
    max_word =''
    for length in range(len(possible)): 
        occ_counter = 0
        for i in range(4): 
            occ_counter += order_letters[i]
        if occ_counter > max_occ: 
            max_occ = occ_counter
            max_word = possible[length]
    print('You should play '. format(max_word))

# Should now have printed the word to play 
# TEST - should print the same word every time for the first go 
# [XXXXX]


# Taking the input as a result of the first word 

result = input('What was the result? (g = green, y = yellow, b = black) ').lower().replace(' ','')
feedback = []

while i in range(4): 
    feedback.append(result_1[i])
if result == 'ggggg':
    print('Complete')

# Starting a new round of the game if not successful 
# Taking arguments as: 
# - Identity of each letters g/y/b/? 

#else: 
    
    #new_round(, not_words)
