#! python3
# bullet-point-adder.py - Adds bullet points to the start of each line on the clipboard.

import xerox

text = xerox.paste()

# Separate lines and add stars.

lines = text.split('\n')
for i in range(len(lines)):
  lines[i] = '* ' + lines[i] 

text = '\n'.join(lines)
print(text)

xerox.copy(text)
