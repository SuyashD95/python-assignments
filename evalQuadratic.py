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