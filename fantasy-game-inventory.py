def displayInventory(inventory):
  print('Inventory:')
  item_total = 0
  for k, v in inventory.items():
    item_total += v
    print(k + ': ' + str(v))
  print('Total number of items: ' + str(item_total))

def displayInventoryItems(inventory):
  print('Inventory items:')
  for item in inventory.keys():
    print(item)

def displayInventoryCount(inventory):
  print('Inventory count:')
  count = 0
  for itemCount in inventory.values():
    count += itemCount
  print(count)

def addToInventory(inventory, items):
  for item in items:
    if item in inventory:
      inventory[item] += 1
    else:
      inventory[item] = 1


def displayLoot(name, loot):
  print(name + ' loot:')
  for item in loot:
    print(item)


myInventory = {
  'rope': 1, 
  'torch': 6, 
  'gold coin': 42, 
  'dagger': 1, 
  'arrow': 12
}

displayInventory(myInventory)
print('')

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
displayLoot('Dragon', dragonLoot)
print('')

addToInventory(myInventory, dragonLoot)
displayInventory(myInventory)
