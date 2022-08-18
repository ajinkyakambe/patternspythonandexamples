# 3. Python Program to Shuffle deckofcard of Cards

# importing modules
import itertools
import random

# make a deckofcard of cards
deckofcard = list(itertools.product(range(1, 14),['Spade', 'Heart', 'Diamond', 'Club']))

# shuffle the cards
random.shuffle(deckofcard)

# draw five cards
print("You got:")
for i in range(5):
   print(deckofcard[i][0], "of", deckofcard[i][1])