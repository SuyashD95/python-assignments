"""
Q3- Write a Python function, clip(lo, x, hi) that returns lo if x is less than lo; hi if x is greater than hi; and x otherwise. For this problem, you can assume that lo < hi. Don't use any conditional statements for this problem. Instead, use the built in Python functions min and max 
"""
# NOTE TO SELF: Naps really work!!!!

def clip( lo, x, hi):

	lo = int( lo )
	x = int( x )
	hi = int( hi )

	if min( lo, x, hi ) == x:
		return lo
	elif max( lo, x, hi ) == x:
		return hi
	else:
		return x

print( "NOTE: For this program to work, the way it is supposed to.. lo is less than hi i.e, lo < hi\n" )

lo = input( "Enter lo: " )
x = input( "Enter x: " )
hi = input( "Enter hi: " )

ans =  str( clip( lo, x, hi ) )
print( "The answer is: " + ans )

