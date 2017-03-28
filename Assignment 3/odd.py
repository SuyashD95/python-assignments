"""
Q4- Write a Python function, odd, that takes in one number and returns True when the number is odd and False otherwise. You should use the % (mod) operator, not if. This function takes in one number and returns a boolean
"""

def odd( number ):

	return number % 2 == 1

number = int( input( "Enter a number: ") )

print( "Is the number " + str( number ) + " odd? Answer: " + str( odd( number) ) ) 
