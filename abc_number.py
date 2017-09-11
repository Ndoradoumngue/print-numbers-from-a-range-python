# program to print numbers from 30 to 300

# function to check the multiplier

def checkMultiplier(number, firstDivider, secondDivider):

	alphabet = 'abcdefghijklmnopqrstuvwxyz'

	if number%firstDivider==0:

		# get the 3 first characters of the alphabet

		output = alphabet[:3]

	elif number%secondDivider==0:

		# get the 3 last characters of the alphabet

		output = alphabet[-3:]

	elif number%firstDivider==0 and number%secondDivider==0:

		output = alphabet[:1]+'-'+alphabet[-1:]
	else:
		output = number

	return output


# main program

fromRange = 30
toRange = 301

divider1 = 7
divider2 = 13

for multiplier in range(fromRange,toRange):

	multiplierInfo = checkMultiplier(multiplier, divider1, divider2)

	print (multiplierInfo)