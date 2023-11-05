#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import math
# Taking Inputs
start = int(input("Enter starting range:- "))

# Taking Inputs
last = int(input("Enter lasting range:- "))


x = random.randint(start,last)
print("\n\tYou've only ", 
	round(math.log(last - start + 1, 2)),
	" chances to guess the integer!\n")

# Initializing the number of guesses.
count = 0


while count < math.log(last - start + 1, 2):
	count += 1

	# taking guessing number as input
	guess = int(input("Guess a number:- "))

	# Condition testing
	if x == guess:
		print("Congratulations you did it in ",
			count, " try")
		# Once guessed, loop will break
		break
	elif x > guess:
		print("You guessed too small!")
        
	elif x < guess:
		print("You Guessed too high!")


if count >= math.log(last - start + 1, 2):
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")




# In[ ]:





# In[ ]:




