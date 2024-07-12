"""
BINARY TO DENARY CONVERSION CHALLENGE

You will need to:
- Write a function that takes in a binary string and returns an integer with its converted value.
- Validate binary strings before conversion
- Identify an error state and throw a custom exception
- Create a test file for the function and create a comprehensive test suite
"""

import math


class Bin2DenException(Exception):
    pass  # Custom exception class for handling non-binary string errors.


def bin2den(binstring):
    b = set(binstring) # Create a set of characters in binstring.
    s = {'0', '1'}  # Define a set of valid binary characters ('0' and '1').
    # Check if all characters in binstring are '0' or '1'.
    if s == b or b == {'0'} or b == {'1'}:
        value = int(binstring, 2) # Convert binary string to integer.
    else:
        raise Bin2DenException("Non Binary String")
    return value


bstr = "10101"
val = bin2den(bstr)  # Call bin2den function to convert binary string.
print(val)  # Print the converted integer value.
