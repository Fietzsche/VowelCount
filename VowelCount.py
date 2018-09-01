# Vowel Count program
# Counts number of vowels in a given piece of text

# Gets string from user
text = input("Type something")

vowelNo = text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u')

print("The text you've entered has " + str(vowelNo) + " vowels in it.")
