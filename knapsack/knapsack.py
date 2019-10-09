#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def quicksort(items):
  if len(items) <= 1:
    return items
  pivot = items[-1]
  left = []
  right = []

  for i in range(len(items) - 1):
    item = items[i]
    item_profit = item.value - item.size
    pivot_profit = pivot.value - pivot.size
    if item_profit > pivot_profit:
      left.append(item)
    else:
      right.append(item)

  return quicksort(left) + [pivot] + quicksort(right)



def knapsack_solver(items, capacity):
  sorted_items = quicksort(items)
  knapsack = []

  while capacity > sorted_items[0].size:
    new_item = sorted_items[0]
    capacity -= new_item.size
    knapsack.append(new_item)
    sorted_items.remove(new_item)

  weight = 0
  value = 0
  chosen = []
  for item in knapsack:
    weight += item.size
    value += item.value
    chosen.append(item.index)
    #print(item.index)

  print(f"weight: {weight}")
  for item in sorted_items:
    print(item.size)

  return {'Value': value, 'Chosen': chosen}
    


  
  
list1 = [Item(1, 42, 81),
  Item(2, 42, 42),
  Item(3, 68, 56),
  Item(4, 68, 25),
  Item(5, 77, 14),
  Item(6, 57, 63),
  Item(7, 17, 75),
  Item(8, 19, 41),
  Item(9, 94, 19),
  Item(10, 34, 12)]

list2 = [Item(1, 18, 100),
  Item(2, 51, 76),
  Item(3, 68, 26),
  Item(4, 44, 79),
  Item(5, 46, 64),
  Item(6, 65, 18),
  Item(7, 66, 1),
  Item(8, 52, 80),
  Item(9, 47, 93),
  Item(10, 3, 66)]




print(knapsack_solver(list1, 100))
print(knapsack_solver(list2, 100))


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')