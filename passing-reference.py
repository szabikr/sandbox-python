def eggs(someParameter):
  print('someParameter id: ' + str(id(someParameter)))
  someParameter.append('Hello')

spam = [1, 2, 3]
print('spam id: ' + str(id(spam)))
eggs(spam)
print(spam)
