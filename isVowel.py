""" Q5- Define a function isVowel(char) that returns True if char is a vowel ('a', 'e', 'i', 'o', or 'u'), and False
otherwise. You can assume that char is a single letter of any case (ie, 'A' and 'a' are both valid). Do not use the
keyword in. Your function should take in a single string and return a boolean. 
"""


def isVowel( char ):

	str.lower( char )
	return char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'

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
