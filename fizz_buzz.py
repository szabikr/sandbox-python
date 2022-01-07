import sys

if len(sys.argv) < 2:
  print('Usage: python3 fizz_buzz.py [count] - print fizz buzz sequence')
  sys.exit()

count = sys.argv[1]

# generate a list with size count
for number in range(int(count) + 1):
  if number == 0:
    continue

  if number % 3 == 0 and number % 5 == 0:
    print('fizzbuzz')
  else:
    if number % 3 == 0:
      print('fizz')
    else:
      if number % 5 == 0:
        print('buzz')
      else:
        print(number)
