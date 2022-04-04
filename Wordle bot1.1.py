
def getwords():
    
    # Getting list of 5 letter words from website 

    from urllib.request import urlopen
    url = "https://gist.githubusercontent.com/cfreshman/cdcdf777450c5b5301e439061d29694c/raw/de1df631b45492e0974f7affe266ec36fed736eb/wordle-allowed-guesses.txt"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html
    
def counting(word):
    letterlist = {}
    alphabet = 'abcdefghijklmonpqrstuvwxyz'
    for letter in alphabet: 
        letterlist[letter] = word.count(letter)
    return letterlist
letterlist = counting(getwords())
print(letterlist)

order =[]

for i in range(26):
    least = 10000
    saved = ''
    for letter,number in letterlist.items():
        if number < least: 
            least = number
            saved = letter
            #print(least)
            #print(saved)
    letterlist[saved] = 10000
    order.append(saved)
print('\n')
print(order)

'''
print(type(getwords()))
''
    return html.split("\n")

for i in range(25): #range(len(getwords())):
    _words.append(getwords()[i])
    #TEST - prints all words 
    print (_words[i])
''
def repeat_let(word): 
    return a(word.count(a) > 1 for a in word)

print(repeat_let('kayan'))
'''

