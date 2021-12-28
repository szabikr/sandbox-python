supplies = ['pens', 'staplers', 'flamethrowers', 'binders']

print('for item in supplies:')
for item in supplies:
  print(item)

print('')
print('for i in range(len(supplies)):')
for i in range(len(supplies)):
  print(supplies[i] + ' is index ' + str(i))

print('')
print('for index, item in enumerate(supplies):')
for index, item in enumerate(supplies):
  print(item + ' is index ' + str(index))
