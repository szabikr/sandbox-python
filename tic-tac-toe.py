theBoard = {
  'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
  'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
  'low-L': ' ', 'low-M': ' ', 'low-R': ' '
}

exampleBoard = {
  'top-L': 'O', 'top-M': 'O', 'top-R': 'O',
  'mid-L': 'X', 'mid-M': 'X', 'mid-R': ' ',
  'low-L': ' ', 'low-M': ' ', 'low-R': 'X'
}

def printBoard(board):
  print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
  print('-+-+-')
  print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
  print('-+-+-')
  print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# TODO: move validation
def validateMove(board, move):
  print('validateMove() not yet implemented')

# TODO: valuate board. Is it a win for X or 0? Is it a draw?
def valuateBoard(board):
  print('valuateBoard() not yet implemented')

turn = 'X'
for i in range(9):
  printBoard(theBoard)
  print('')
  print('Turn for ' + turn + '. Move on which space?')
  move = input()
  theBoard[move] = turn
  if turn == 'X':
    turn = 'O'
  else:
    turn = 'X'

printBoard(theBoard)
