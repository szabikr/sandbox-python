import sys

if len(sys.argv) < 2:
  print('Usage: python3 mclip.py [keyphrase] - copy phrase text')
  sys.exit()

keyphrase = sys.argv[1]

print(keyphrase)
