#Hindi to English translation 

a = {
    "gadi": "car",
    "insaan": "human",
    "ladka": "boy",
    "ladki": "girl"
}

m = input("enter the word to be translated (or 1 to see all words): ")

if m == "1":
    print(a)
else:
    translation = a.get(m)
    if translation:
        print(translation)
    else:
        print("Word not found in the dictionary.")
