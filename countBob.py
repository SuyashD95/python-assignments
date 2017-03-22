""" Q7- Assume s is a string of lower case characters. Write a program that
prints the number of times the string 'bob' occurs in s. For example, if s =
'azcbobobegghakl', then your program should print Number of times bob occurs
is: 2  
"""

def countBob( string ):

	count = 0
	start = 0

	while string.find( "bob" ) != -1:

		start = string.find( "bob" ) # Finds the first character where the substring "bob" first appears.
		
		# Strings are immutable. Hence, we store the new string by slicing the existing string from position start + 1 to the last position(length of string - 1)
		string = string[ start + 1 : ]
		count += 1

	return count

print( "Remember all the characters in the string should be in LOWERCASE" )
string = input( "Enter the string: ")
print( "Number of times bob occurs is: " + str( countBob( string ) ) )

# Uncomment the following line if you are using Console/Terminal
# input("Press any key to exit..." )
