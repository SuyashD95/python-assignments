"""
Q1- Write a Python function, square, that takes in one number and returns the square of that number.
""" 

def square( num ):
	n = int( num )
	return n ** 2

n = input( "Write a number: " )
print( "Square of a number " + n + ": " + str( square( n ) ) )