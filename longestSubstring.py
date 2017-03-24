""" 
Q8- Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For
example, if s = 'azcbobobegghakl', then your program should print Longest substring in alphabetical order is: beggh In
the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print Longest
substring in alphabetical order is: abc 
"""

def longestSubstring( string ):


	string = str.lower( string )
	
	longest_string = ""
	max_length = 0
	current_string = ""
	
	outer = 0

	print( "Length of original string: " + str( len( string ) ) )
	while outer < len( string ):

		print( "In position " +  str( outer ) + ": " + string[ outer ] )
		print( "Entered the outer loop." )

		if outer + 1 != len( string ) and string[ outer ] < string[ outer + 1]:
			
			print( "Entered the first If..." )
			inner = outer
			print("Outer 1: " + str( outer ) + "; Inner 1: " + str( inner ) )

			while True:

				print( "Entered the inner loop" )
				inner += 1
				print( "Inner 2: " + str( inner ) )

				if inner < len( string ):

					print( "Entered the second If..." )
					if inner + 1 != len(string) and string[ inner ] > string[ inner + 1 ]:

						print( "Entered the third If..." )
						break
					else:

						print( "Entered the third Else...." )
						if string[ inner ] > string[ inner - 1 ]:
							
							print( "Entered the fourth If...." )
							break
						else:
							print( "Entered the fourth Else...." )
				else:
					
					print( "Entered the second Else...." )

			print( "Exited the inner loop" )
			current_string = string[ outer : inner ]
			outer = inner
			print("Outer 2: " + str( outer ) )

		else:

			print(" Entered the first Else...")
			
			if len( string ) == 1 or outer + 1 != len( string ) and string[ outer ] > string[ outer + 1]:
				print( " Length is 1 or the letter, along with the first next one are in alphabetical order..")
				current_string = string[outer]

			if len( current_string ) > max_length:
				longest_string = current_string
				max_length = len(longest_string)
				current_string = ""

			outer += 1


	print("Longest substring in alphabetical order: " + longest_string )

longestSubstring( "ab" )
input( "Enter any key to exit..." )
