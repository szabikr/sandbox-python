l = [3] * 11

print('for loop')
for i in l:
  print(i)

print('list comprehension')
[print(i) for i in l]

a = 'the result is' + ('true' if len(l) == 10 else 'false')

print('evaluation: ', a)
