# Vowel Count program
# Counts number of vowels in a given piece of text

# Gets string from user
text = input("Type something\n")

vowelNo = text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u')
vowelNoY = vowelNo + text.count('y')

# Determines if "Vowel" or "Vowels" is used from whether or not there's only 1 vowel
if vowelNo > 1:
    vowelText = " vowels"
elif vowelNo <= 1:
    vowelText = " vowel"

# Adds extra text if y is in the string, as it's sometimes a vowel
if 'y' not in text:
    print("The text you've entered has " + str(vowelNo) + vowelText + " in it.")
elif 'y' in text:
    print("The text you've entered has " + str(vowelNo) + vowelText + " in it.")
    print("(" + str(vowelNoY) + " if you count y)")
