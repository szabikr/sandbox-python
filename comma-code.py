def commaCode(array):
  result = ''
  for index in range(len(array)):
    if result == '':
      result += str(array[index])
      continue
    if index == len(array) - 1:
      result += ', and ' + str(array[index])
      continue
    result += ', ' + str(array[index])
  
  return result

spam = ['apples', 'bananas', 'tofu', 'cats']
print('spam', spam)
print(commaCode(spam))

test1 = []
print('test 1', test1)
print(commaCode(test1))

test2 = ['just_apples']
print('test 2', test2)
print(commaCode(test2))

test3 = ['apples', 'bananas']
print('test 3', test3)
print(commaCode(test3))

test4 = [1, 2, 3, 4, 5]
print('test 4', test4)
print(commaCode(test4))
