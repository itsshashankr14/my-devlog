#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    """
    Function to capitalize the first letter of each word in the string,
    while preserving the original spacing and format.
    
    Args:
    s (str): Input string containing full name or sentence
    
    Returns:
    str: Capitalized string with original formatting preserved
    """

    # re.sub is used here to find all 'words' using the regex pattern \b\w+
    # \b     → Word boundary (start of a word)
    # \w+    → One or more alphanumeric characters (a-z, A-Z, 0-9, _)
    # match.group(0) gets the matched word, and .capitalize() turns the first letter uppercase
    return re.sub(r'\b\w+', lambda match: match.group(0).capitalize(), s)

if __name__ == '__main__':
    # Open the output file defined by the environment (used in online judges like HackerRank)
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Take the full name as input from user
    s = input()

    # Call the solve function to get the capitalized result
    result = solve(s)

    # Write the result to the output file (used for submission evaluation)
    fptr.write(result + '\n')

    # Close the file after writing
    fptr.close()
