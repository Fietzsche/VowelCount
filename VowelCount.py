# Vowel Count program
# Counts number of vowels in a given piece of text

text = input("Type something\n")

# Converts text to lowercase so vowel counting won't be case sensitive
lowerText = text.lower()

vowelNo = lowerText.count('a') + lowerText.count('e') + lowerText.count('i') + lowerText.count('o') + lowerText.count('u')
vowelNoY = vowelNo + lowerText.count('y')

# Determines if "Vowel" or "Vowels" is used from whether or not there's only 1 vowel
if vowelNo > 1 or vowelNo == 0:
    vowelText = " vowels"
elif vowelNo == 1:
    vowelText = " vowel"

print("The text you've entered has " + str(vowelNo) + vowelText + " in it.")

# Adds extra text if y is in the string, as it's sometimes a vowel
if 'y' in lowerText:
    print("(" + str(vowelNoY) + " if you count Y)")
