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

def printResults(board):
  print('')
  print('')
  print('The Results are in')
  print('==================')
  result = valuateBoard(board)
  if result == True:
    print('Draw')
  else:
    print('Winner: ' + result)

def pickSymbol():
  print('Pick your symbol (X or O):')
  turn = input()
  while turn != 'X' and turn != 'O':
    if turn == 'x':
      return 'X'
    if turn == 'o':
      return 'O'
    print('pick X or O')
    turn = input()
  return turn

def isBoardFull(board):
  for v in board.values():
    if v == ' ':
      return False
  return True

def valuateBoard(board):

  # Check horrizontally
  if board['top-L'] != ' ' and board['top-L'] == board['top-M'] and board['top-M'] == board['top-R']: 
    return board['top-L']
  
  if board['mid-L'] != ' ' and board['mid-L'] == board['mid-M'] and board['mid-M'] == board['mid-R']: 
    return board['mid-L']

  if board['low-L'] != ' ' and board['low-L'] == board['low-M'] and board['low-M'] == board['low-R']: 
    return board['low-L']

  # Check vertically
  if board['top-L'] != ' ' and board['top-L'] == board['mid-L'] and board['mid-L'] == board['low-L']:
    return board['top-L']
  
  if board['top-M'] != ' ' and board['top-M'] == board['mid-M'] and board['mid-M'] == board['low-M']:
    return board['top-M']
  
  if board['top-R'] != ' ' and board['top-R'] == board['mid-R'] and board['mid-R'] == board['low-R']:
    return board['top-R']

  # Check crosses
  if board['top-L'] != ' ' and board['top-L'] == board['mid-M'] and board['mid-M'] == board['low-R']:
    return board['top-L']
  
  if board['top-R'] != ' ' and board['top-R'] == board['mid-M'] and board['mid-M'] == board['low-L']:
    return board['top-R']

  return isBoardFull(board)


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
  while valuateBoard(board) == False:
    printBoard(board)
    print('')
    
    while True:
      print('Turn for ' + turn + '. Pick a square')
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
turn = pickSymbol()
printDefinition()
game(theBoard, turn)
printResults(theBoard)
