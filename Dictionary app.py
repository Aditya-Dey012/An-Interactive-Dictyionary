import json
from difflib import get_close_matches

data = json.load(open("Data.json"))

def translator(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        x=input("Did you mean %s instead? Type Y if yes, N if no or you may type the correct word again:" %get_close_matches(w, data.keys())[0])
        if x == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif  x== "N":
            return "Sorry, we couldn't help you."
        else:
            return translator(x)
    else:
        return "\nThe word you typed doesn't exist. Please type a correct word."
    
word = input("Enter the word:")

output=translator(word)

if type(output)== list:
    for i in output:
        print (i)
else:
    print(output)

