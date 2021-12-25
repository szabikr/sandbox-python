theBoard = {
  'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
  'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
  'low-L': ' ', 'low-M': ' ', 'low-R': ' '
}

def printWelcome():
  print('')
  print('')
  print('Welcome to Tic-Tac-Toe')
  print('======================')

def printDefinition():
  print('')
  print('')
  print('Location Definitions')
  print('=====================')
  print('')
  print('top-L ' + '|' + ' top-M ' + '|' + ' top-R')
  print('------+-------+------')
  print('mid-L ' + '|' + ' mid-M ' + '|' + ' mid-R')
  print('------+-------+------')
  print('low-L ' + '|' + ' low-M ' + '|' + ' low-R')

def printBoard(board):
  print('')
  print('')
  print('Current Board')
  print('=============')
  print('')
  print('  ' + board['top-L'] + ' | ' + board['top-M'] + ' | ' + board['top-R'] + ' ')
  print(' ---+---+---')
  print('  ' + board['mid-L'] + ' | ' + board['mid-M'] + ' | ' + board['mid-R'] + ' ')
  print(' ---+---+---')
  print('  ' + board['low-L'] + ' | ' + board['low-M'] + ' | ' + board['low-R'] + ' ')

# TODO: valuate board. Is it a win for X or 0? Is it a draw?
def valuateBoard(board):
  print('valuateBoard() not yet implemented')

def isBoardFull(board):
  for v in board.values():
    if v == ' ':
      return False
  return True

def registerMove(board, move, turn):
  if move == 'top-M' or move == 'mid-M' or move == 'low-M':
    board[move] = ' ' + turn + ' '
    return
  
  if move == 'top-L' or move == 'mid-L' or move == 'low-L':
    board[move] =  turn + ' '
    return
  
  if move == 'top-R' or move == 'mid-R' or move == 'low-R':
    board[move] = ' ' + turn
    return

def game(board, turn):
  while isBoardFull(board) == False:
    printBoard(board)
    print('')
    
    while True:
      print('Turn for ' + turn + '. Move on which space?')
      move = input()
      if move in board.keys() and board[move] == ' ':
        board[move] = turn
        break
      print('Incorrect move')      

    if turn == 'X':
      turn = 'O'
    else:
      turn = 'X'

  printBoard(board)

printWelcome()

print('pick you symbol (X or O):')
turn = input()
while turn != 'X' and turn != 'O':
  print('pick X or O')
  turn = input()

printDefinition()
game(theBoard, turn)
