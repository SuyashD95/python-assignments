def odd( number ):

	return number % 2 == 1

number = int( input( "Enter a number: ") )

print( "Is the number " + str( number ) + " odd? Answer: " + str( odd( number) ) ) 
