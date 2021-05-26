"""
    Prefer Interpolated F-Strings Over C-style Format Strings and str.format
"""

# Defining binary and hexadecimal variables
binary = 0b10111011
hexadecimal = 0xc5f

if __name__ == '__main__':
    # Converting binary and hexadecimal values to integer strings
    print("Binary is %d, hexadecimal is %d" % (binary, hexadecimal))
