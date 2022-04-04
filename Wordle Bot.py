def getwords():
    from urllib.request import urlopen
    url = "https://gist.githubusercontent.com/cfreshman/cdcdf777450c5b5301e439061d29694c/raw/de1df631b45492e0974f7affe266ec36fed736eb/wordle-allowed-guesses.txt"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html.split("\n")
    
words = []
letterlist = {}

for i in range(5):#range(len(getwords())):
    words.append(getwords()[i])
    print (words[i])

    for l in range(5): 
        if words[i][l] in letterlist: 
            letterlist[words[i][l]] += 1 
        else: 
            letterlist[words[i][l]] = 1
    print(letterlist)
