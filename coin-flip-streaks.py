import random

# required streak length
REQUIRED_STREAK_LENGTH = 6

test1 = ['tails', 'tails', 'tails', 'tails', 'tails', 'tails'] # should be 1
test2 = ['tails', 'tails', 'tails', 'tails', 'heads', 'tails'] # should be 0
test3 = ['tails', 'tails', 'tails', 'tails', 'tails', 'tails', 'tails'] # should be 2

def getCoinFlips(numberOfFlips):
  result = []
  for filpNumber in range(numberOfFlips):
    flip = 'heads' if random.randint(0, 1) == 0 else 'tails'
    result.append(flip)
  return result

numberOfStreaks = 0
for experimentNumber in range(10000):
  coinFlips = getCoinFlips(100)

  streakCount = 0
  for index, coinFlip in enumerate(coinFlips):
    if index == 0:
      streakCount += 1
      continue

    if coinFlip == coinFlips[index - 1]:
      streakCount += 1
    else:
      streakCount = 0
    
    if streakCount >= REQUIRED_STREAK_LENGTH:
      numberOfStreaks += 1

print('Number of Streaks: ' + str(numberOfStreaks))
