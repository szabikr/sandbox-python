def getMaxCellLen(column):
  maxCellLen = 0
  for cell in column:
    if len(cell) > maxCellLen:
      maxCellLen = len(cell)
  return maxCellLen

def printTable(tableData, title):
  print('\n' + str(title) + ':\n')

  maxCellLens = []
  [maxCellLens.append(getMaxCellLen(column)) for column in tableData]

  for i in range(len(tableData[0])):
    for j in range(len(tableData)):
      print(tableData[j][i].rjust(maxCellLens[j] + 1).ljust(maxCellLens[j] + 2), end=' ')
    if i == 0:
      """ Print Divider """
      print('')
      for index, maxCellLen in enumerate(maxCellLens):
        print(''.center(maxCellLen + 2, '-'), end='+' if index != len(maxCellLens) - 1 else '')
    print('')

# Value of tableData will be changed after performing this function
def addHeaderToTable(tableData, tableHeaders):
  for i in range(len(tableData)):
    tableData[i] = [tableHeaders[i]] + tableData[i]
