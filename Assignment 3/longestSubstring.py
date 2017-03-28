""" 
Q8- Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For
example, if s = 'azcbobobegghakl', then your program should print Longest substring in alphabetical order is: beggh In
the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print Longest
substring in alphabetical order is: abc 
"""


def longestSubstring(string):

    str.lower(string)
    longest_substring = ""

    # Work area STARTS

    current_string = ""
    previous_char = ""

    # Using enumerate to retrieve the index of a specific character of the
    # string, along with the character itself.
    for index, letter in enumerate(string):

        # print( "The letter " + letter + " is at index " + str( index ) )

        # Section 1: If it's the first element of the string, then, assign its
        # value to previous_char.

        if index == 0:
            previous_char = letter

        """ 
		Section 2A: If the current letter is the same or comes after the current previous letter according to the
		English alphabet, then add it to the current string. 

		Section 2B: Otherwise, compare the length of the existing current_string to the length of the longest_substring, then assign
		it and then, discard the existing current_string and assign the current letter. """

        if letter >= previous_char:
            current_string += letter
        else:
            if len(current_string) > len(longest_substring):
                longest_substring = current_string
            current_string = letter
       
        """
		Section 3: If the current string is the longest alphabetical substring, assign it to longest_substring. """
        if len(current_string) > len(longest_substring):
            longest_substring = current_string
       
        """ 
		Section 4: Replace the previous letter with the current one, in case, it's not the last or the first element of the string. """
        if index != 0 and index != len(string) - 1:
            previous_char = letter

    # Work area ENDS

    print("Longest substring in alphabetical order is: " + longest_substring)


string = input("Enter a string: ")
longestSubstring(string)
