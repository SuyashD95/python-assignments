""" Q6- Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i',
'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print: Number of vowels: 5
"""

# Using the isVowel function from isVowel.py module (Answer of fifth question of Assignment 3)
def isVowel( char ):

	# Converting the letter to lowercase for our convenience and hence, we do not need to check character's case and hence, simplifies the problem
	# str.lower( char ) 
	# The above function has been commented out since this is not required in this problem.. But, the above built-in function might be useful in normal cases.

	# Splitting the condition: 'a' or 'e'  or 'i' or 'o' or 'u' to make it more readable and easier to understand. 
	
	is_char_a = char == 'a'
	is_char_e = char == 'e'
	is_char_i = char == 'i'
	is_char_o = char == 'o'
	is_char_u = char == 'u'

	is_char_vowel = is_char_a or is_char_e  or is_char_i or is_char_o or is_char_u 
	
	return is_char_vowel


def countVowels( string ):

	if str.islower( string ):

		count = 0 # Counts the number of vowels
		for letter in string:

			if isVowel( letter ):
				count += 1
		
		print( "Number of vowels: " + str( count ) )
	else:

		if len( string ):
			print( "Error: All the characters in the string should be in LOWERCASE." )
		else:
			print( "Error: The string is EMPTY." )

string = input( "Enter the string: " )
countVowels( string )