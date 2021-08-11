no_vowels = ""
new_word = input("Please type a word: ")
new_word = new_word.upper()

for letter in new_word:
    if letter=="A":
        continue
    elif letter=="E":
        continue
    elif letter=="I":
        continue
    elif letter=="O":
        continue
    elif letter=="U":
        continue
    else: no_vowels += letter        
print(no_vowels)