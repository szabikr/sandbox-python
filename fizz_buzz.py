import sys

if len(sys.argv) < 2:
  print('Usage: python3 fizz_buzz.py [count] - print fizz buzz sequence')
  sys.exit()

count = sys.argv[1]

def fizzBuzz(number):
  if number % 3 == 0 and number % 5 == 0:
    return 'fizzbuzz'
    
  if number % 3 == 0:
    return 'fizz'

  if number % 5 == 0:
    return 'buzz'
    
  return number

# generate a list with size count
for number in range(int(count) + 1):
  if number == 0:
    continue

  print(fizzBuzz(number))
