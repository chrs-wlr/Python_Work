#ENCYcloPEDIA
#encyCLOpedia

word = "encyclopedia"
new_word = word.upper()
final_word = new_word.replace("CLO","clo")

print(final_word)

word = "encyclopedia"
new_word = word.lower()
final_word = new_word.replace("clo","CLO")

print(final_word)


#ALT METHOD

word = "EnCycloPedIa"
print(word[:3].upper() + word[3:6].lower() + word[6:].upper())
print(word[:3].lower() + word[3:6].upper() + word[6:].lower())