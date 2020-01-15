# Children's activities

# Define four Python functions named run, swing, slide, and hide_and_seek. Each function should take a child's name as an argument. Each function should print that the child performed the activity.
# For example, Jay ran like a fool! or Chantelle slid down the slide!.
# The following lists of children should be iterated, and the names sent to the appropriate functions.
running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

def run():
		for kid in running_kids:
				print(f'{kid} was running like a fool.')

def swing():
		for kid in swinging_kids:
				print(f'{kid} swung into the night + was never seen again.')

def slide():
		for kid in sliding_kids:
				print(f'{kid} slid down the slide!')

def hide():
		for kid in hiding_kids:
				print(f'{kid} hid from the teach.')

run(), swing(), slide(), hide()

# ChickenMonkey

# Write a program that prints the numbers from 1 to 100. You can use Python's range() to quickly make a list of numbers.
# For multiples of five (5, 10, 15, etc.) print "Chicken" instead of the number
# For the multiples of seven (7, 14, 21, etc.) print "Monkey".
# For numbers which are multiples of both five and seven print "ChickenMonkey".
# To determine if a number can be evenly divided by 5 or 7, use the Python modulo operator.

def chicken_monkey():
		for num in range(1,101):
				if not num%5 and not num%7:
						print('Chicken Monkey')
						continue
				if not num%5:
						print('Chicken')
						continue
				if not num%7:
						print('Monkey')
						continue
				else:
						print(num)

# Coins

# Create a function called calc_dollars. In the function body, define a dictionary and store it in a variable named piggyBank. The dictionary should have the following keys defined: quarters, nickels, dimes, pennies.
# For each coin type, give yourself as many as you like.
# Once you have given yourself a large stash of coins in your piggybank, look at each key and perform the appropriate math on the integer value to determine how much money you have in dollars. Store that value in a variable named dollarAmount and print it.
# Given the coins shown above, the output would be 7.07 when you call calc_dollars()

def calc_dollars(bank):
		values = { "pennies": .01, "nickels": .05, "dimes": .1, "quarters": .25 }
		total = 0

		for coins in bank:
				total += bank[coins] * values[coins]

		print(total)

piggyBank = {
    "pennies": 342,
    "nickels": 9,
    "dimes": 32
}

calc_dollars(piggyBank)

# Now the opposite
import math

def calc_bank(amount):
		bank = { "pennies": 0, "nickels": 0, "dimes": 0, "quarters": 0 }

		bank["quarters"] = amount//.25
		amount -= bank["quarters"]*.25
		bank["dimes"] = amount//.1
		amount -= bank["dimes"]*.1
		bank["nickels"] = amount//.05
		amount -= bank["nickels"]*.05
		bank["pennies"] = math.ceil(amount/.01)
		print(bank)

calc_bank(8.69)