""" 
Q8- Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For
example, if s = 'azcbobobegghakl', then your program should print Longest substring in alphabetical order is: beggh In
the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print Longest
substring in alphabetical order is: abc 
"""

def longestSubstring( string ):

	str.lower( string )
	longest_substring = ""

	print( "Longest substring in alphabetical order is: " + longest_substring )


string = input( "Enter a string: " )
longestSubstring( string )