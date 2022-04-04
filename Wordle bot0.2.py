
# Getting list of 5 letter words from website 

def getwords():
    from urllib.request import urlopen
    url = "https://gist.githubusercontent.com/cfreshman/cdcdf777450c5b5301e439061d29694c/raw/de1df631b45492e0974f7affe266ec36fed736eb/wordle-allowed-guesses.txt"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html.split("\n")
    
words = []
letterlist = {}

# Adding the words into a dictionary {letters: number of total occurances}

for i in range(5) #range(len(getwords())):
    words.append(getwords()[i])
    print (words[i])

    for l in range(5): 
        if words[i][l] in letterlist: 
            letterlist[words[i][l]] += 1 
        else: 
            letterlist[words[i][l]] = 1

#TEST - should print in order: 
# [XXXXX]
print(letterlist)

order_letters = []

# Ordering the letters according to the number of their occurances - least to most common 

for times in range(26): 

    most_let = ''
    most_num = 

    for letter, number in letterlist: 
        if number < var: 
             least_num = number
             least_let = letter
        letterlist.pop(least_let)
        order_letters.append(least_let) 

#TEST - should print in order of least common to most common: 
# [XXXXX]

print(order_letters)




# Should remove all words where there are repeats of the same letter 




possible = words
var = 0

# Finding list of possible words by removing words with the least common letters 
# Do this until only 1 word or there are only 5 letters left 

while len(possible) > 1 and var <= 22: 
    for length in range(len(possible)): 
       if order_letters[var] in possible[length]: 
            possible.remove(possible[length])
    var += 1


