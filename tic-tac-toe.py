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

def checkTilesForClosing(ai, aiTiles, playerTiles):
  print(ai + ' tiles')
  aiTileCounts = []
  for i in set(aiTiles):
    count = 0
    for j in aiTiles:
      if i == j:
        count += 1
    aiTileCounts.append({ 'tile': i, 'count': count })

  for tile in aiTileCounts:
    if tile['count'] == 2 and tile['tile'] not in playerTiles:
      print('good position to step somewher: ' + tile['tile'])
      if tile['tile'] in ['top', 'mid', 'low']:
        nextStep = ''
        if 'L' not in aiTiles:
          nextStep = tile['tile'] + '-' + 'L'
        if 'M' not in aiTiles:
          nextStep = tile['tile'] + '-' + 'M'
        if 'R' not in aiTiles:
          nextStep = tile['tile'] + '-' + 'R'
      
      if tile['tile'] in ['L', 'M', 'R']:
        if 'top' not in aiTiles:
          nextStep = 'top' + '-' + tile['tile']
        if 'mid' not in aiTiles:
          nextStep = 'mid' + '-' + tile['tile']
        if 'low' not in aiTiles:
          nextStep = 'low' + '-' + tile['tile']

      print('Next step should be: ' + nextStep)
      return nextStep

    print(tile)
  
  return ''

def getAiMove(board, ai):
  if board['mid-M'] == ' ':
    return 'mid-M'
  
  aiTiles = []
  playerTiles = []
  for tile in board.keys():
    if board[tile] == ' ':
      continue
    
    if board[tile] == ai:
      aiTiles += tile.split('-')
    else:
      playerTiles += tile.split('-')

  print('')
  print('attack')
  nextStep = checkTilesForClosing(ai, aiTiles, playerTiles)
  if nextStep != '':
    return nextStep
  
  print('')
  print('defence')
  nextStep = checkTilesForClosing('X' if ai == 'O' else 'O', playerTiles, aiTiles)
  if nextStep != '':
    return nextStep

  return random.choice(list(board.keys()))

def game(board, player, ai):
  turn = 'X'
  while valuateBoard(board) == False:
    printBoard(board)
    print('')
    
    while True:
      print('Turn for ' + ('player(' + turn + ')' if turn == player else 'ai(' + turn + ')') + '. Pick a square')
      if turn == player:
        # move = input()
        move = getAiMove(board, player)

        # while player move is also ai
        print(move)
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
    
    # while player move is also ai
    input()

  printBoard(board)

printWelcome()
player = pickSymbol()
ai = getAiSymbol(player)
printDefinition()
game(theBoard, player, ai)
printResults(theBoard, player)
