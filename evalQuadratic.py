"""
Q2- Write a Python function, evalQuadratic(a, b, c, x), that returns the value of the quadratic  a*x2+b*x+c. This function takes in four numbers and returns a single number. 
"""

def evalQuadratic( a, b, c, x ):

	a = int ( a )
	b = int ( b )
	c = int ( c )
	x = int ( x )

	s = (a * (x ** 2)) + (b * x) + c
	return s

a = input( "Enter a: " )
b = input( "Enter b: " )
c = input( "Enter c: " )
x = input( "Enter x: " )

print( "The answer of the quadratic equation is " + str( evalQuadratic( a, b, c, x ) ) )