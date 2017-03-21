""" Q5- Define a function isVowel(char) that returns True if char is a vowel ('a', 'e', 'i', 'o', or 'u'), and False
otherwise. You can assume that char is a single letter of any case (ie, 'A' and 'a' are both valid). Do not use the
keyword in. Your function should take in a single string and return a boolean. 
"""


def isVowel( char ):

	# Converting the letter to lowercase for our convenience and hence, we do not need to check character's case and hence, simplifies the problem
	str.lower( char ) 

	# Splitting the condition: 'a' or 'e'  or 'i' or 'o' or 'u' to make it more readable and easier to understand. 
	
	is_char_a = char == 'a'
	is_char_e = char == 'e'
	is_char_i = char == 'i'
	is_char_o = char == 'o'
	is_char_u = char == 'u'

	is_char_vowel = is_char_a or is_char_e  or is_char_i or is_char_o or is_char_u 
	
	return is_char_vowel

def isStringContainsVowel( string ):

	i = 0
	while i < len( string ):
		
		letter = string[i]
		
		if isVowel( letter ):
			return True
		
		i += 1

	return False
	

string = input( "Enter a string: " )

print( "Is the string, '" + string + "' contains a vowel in it? Answer: " + str( isStringContainsVowel( string ) ) )
