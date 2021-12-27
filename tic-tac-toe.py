import random

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

def printResults(board, player):
  print('')
  print('')
  print('The Results are in')
  print('==================')
  result = valuateBoard(board)
  if result == True:
    print('Draw')
  else:
    print('Winner: ' + ('player' if result == player else 'ai'))

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

def getAiSymbol(player):
  if player == 'X':
    return 'O'
  return 'X'

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

# checks tiles vertically and horizontally for closing
def checkTilesForClosing(aiTiles, playerTiles, board):
  aiTileCounts = []
  for i in set(aiTiles):
    count = 0
    for j in aiTiles:
      if i == j:
        count += 1
    aiTileCounts.append({ 'tile': i, 'count': count })

  for tile in aiTileCounts:
    if tile['count'] == 2 and tile['tile'] not in playerTiles:
      if tile['tile'] in ['top', 'mid', 'low']:
        if board[tile['tile'] + '-' + 'L'] == ' ':
          return tile['tile'] + '-' + 'L'
        if board[tile['tile'] + '-' + 'M'] == ' ':
          return tile['tile'] + '-' + 'M'
        if board[tile['tile'] + '-' + 'R'] == ' ':
          return tile['tile'] + '-' + 'R'
      
      if tile['tile'] in ['L', 'M', 'R']:
        if board['top' + '-' + tile['tile']] == ' ':
          return 'top' + '-' + tile['tile']
        if board['mid' + '-' + tile['tile']] == ' ':
          return 'mid' + '-' + tile['tile']
        if board['low' + '-' + tile['tile']] == ' ':
          return 'low' + '-' + tile['tile']
  
  return ''

def checkCrosses(board, ai): 
  if board['top-L'] == ai and board['mid-M'] == ai:
    if board['low-R'] == ' ':
      return 'low-R'
  if board['top-L'] == ai and board['low-R'] == ai:
    if board['mid-M'] == ' ':
      return 'mid-M'
  if board['mid-M'] == ai and board['low-R'] == ai:
    if board['top-L'] == ' ':
      return 'top-L'
      
  if board['top-R'] == ai and board['mid-M'] == ai:
    if board['low-L'] == ' ':
      return 'low-L'
  if board['top-R'] == ai and board['low-L'] == ai:
    if board['mid-M'] == ' ':
      return 'mid-M'
  if board['mid-M'] == ai and board['low-L'] == ai:
    if board['top-R'] == ' ':
      return 'top-R'

  return ''

def getAiMove(board, ai):
  aiTiles = []
  playerTiles = []
  for tile in board.keys():
    if board[tile] == ' ':
      continue
    
    if board[tile] == ai:
      aiTiles += tile.split('-')
    else:
      playerTiles += tile.split('-')

  nextStep = checkTilesForClosing(aiTiles, playerTiles, board)
  if nextStep != '':
    print('')
    print('horrizontal & vertical offence')
    return nextStep
  
  nextStep = checkTilesForClosing(playerTiles, aiTiles, board)
  if nextStep != '':
    print('')
    print('horrizontal & vertical defence')
    return nextStep

  nextStep = checkCrosses(board, ai)
  if nextStep != '':
    print('')
    print('cross offence')
    return nextStep

  nextStep = checkCrosses(board, 'X' if ai == 'O' else 'O')
  if nextStep != '':
    print('')
    print('cross defence')
    return nextStep

  nextStep = 'mid-M'
  while board[nextStep] != ' ':
    nextStep = random.choice(list(board.keys()))
  
  return nextStep

def game(board, player, ai):
  turn = 'X'
  while valuateBoard(board) == False:
    printBoard(board)
    print('')
    
    while True:
      print('Turn for ' + ('player(' + turn + ')' if turn == player else 'ai(' + turn + ')') + '. Pick a square')
      if turn == player:
        move = input()
      else:
        move = getAiMove(board, ai)
        print(move)

      if move in board.keys() and board[move] == ' ':
        board[move] = turn
        break
      print('Incorrect move')

    if turn == player:
      turn = ai
    else:
      turn = player

  printBoard(board)

printWelcome()
player = pickSymbol()
ai = getAiSymbol(player)
printDefinition()
game(theBoard, player, ai)
printResults(theBoard, player)
