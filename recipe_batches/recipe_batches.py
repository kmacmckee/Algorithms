#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  rec_count = 0
  ing_count = 0
  print(recipe)

  for item in recipe:
    rec_count += 1

  for item in ingredients:
    ing_count += 1

  if rec_count > ing_count:
    return 0

  total = 1000000
  for r in recipe:

    if int(ingredients[r] / recipe[r]) < total:
      total = int(ingredients[r] / recipe[r])

  return total
    
    
      


      



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 350, 'butter': 120, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))