
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

#TEST
print(letterlist)

most_letters = []

# Gathering the 6 most common letters in the dictionary and adding to a list 
# 6 in case the 5 aren't in a word 

for times in  range(6): 

    most_let = ''
    most_num = 0

    for letter, number in letterlist: 
        if number > var: 
             most_num = number
             most_let = letter
        most_letters.append(most_let) 





