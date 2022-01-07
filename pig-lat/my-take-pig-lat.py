#! python3
# My take on English to Pig Latin translation
# --------- A memorization exercise ---------

print('Enter the English message to translate into Pig Latin')

message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = []

for word in message.split():
  
  nonLetterPrefix = ''
  while len(word) > 0 and not word[0].isalpha():
    nonLetterPrefix += word[0]
    word = word[1:]
  if len(word) == 0:
    pigLatin.append(nonLetterPrefix)
    continue
  
  nonLetterSuffix = ''
  while len(word) > 0 and not word[-1].isalpha():
    nonLetterSuffix += word[-1]
    word = word[:-1]
  
  isUpper = word.isupper()
  isTitle = word.istitle()

  word = word.lower()

  prefixConsonants = ''
  while len(word) > 0 and not word[0] in VOWELS:
    prefixConsonants += word[0]
    word = word[1:]
  
  if prefixConsonants != '':
    word += prefixConsonants + 'ay'
  else:
    word += 'yay'

  if isUpper:
    word = word.upper()
  
  if isTitle:
    word = word.title()

  pigLatin.append(nonLetterPrefix + word + nonLetterSuffix)

print(' '.join(pigLatin))
