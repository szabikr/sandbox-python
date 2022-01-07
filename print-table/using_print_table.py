from print_table import printTable, addHeaderToTable

theTableData = [
  ['apples', 'oranges', 'cherries', 'banana'],
  ['Alice', 'Bob', 'Carol', 'David'],
  ['dogs', 'cats', 'moose', 'goose']
]
theTitle = 'First table'
theTableHeaders = ['Fruits', 'People', 'Animals']

addHeaderToTable(theTableData, theTableHeaders)

printTable(theTableData, theTitle)

