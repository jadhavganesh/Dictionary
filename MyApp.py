import json
from difflib import  get_close_matches
data = json.load(open("data.json"))

def translate(word):
    word = word.lower()     #making word case insensitive
    if word in data:
        return(data[word])
    elif len(get_close_matches(word,data.keys())) > 0:
        yn = input("\nDid you mean %s instead ? if yes 'Y' or no 'N' : " % get_close_matches(word,data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == 'N':
            return "Word Doesn't exists"
        else:
            return "Wrong input"
    else:
        return "Word doesn't exist"

inputWord = input("enter the word : ")
output = translate(inputWord)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
