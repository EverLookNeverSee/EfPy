"""
    Knowing the difference between bytes and str

        there are two types that represent sequences of character data: bytes and str.
        Instances of bytes contain raw, unsigned 8-bit values (often displayed in the
        ASCII encoding). Instances of str contain Unicode code points that represent
        textual characters from human languages.
"""

from typing import Union


# Defining a byte
my_byte = b"h\x65llo"
print(f"list of my_byte: {list(my_byte)}")
print(f"type of my_byte: {type(my_byte)}")
print(f"my_byte: {my_byte}")

# This is the output separator
print("*-*" * 50)

# Defining a string
my_string = "a\u0300 python"
print(f"list of my_byte: {list(my_string)}")
print(f"type of my_byte: {type(my_string)}")
print(f"my_byte: {my_string}")


def to_str(bytes_or_str: Union[bytes, str]) -> str:
    """
    This function takes a bytes or string instance and always returns a str
    :param bytes_or_str: bytes or str instance
    :return: str instance
    """
    if isinstance(bytes_or_str, bytes):
        result = bytes_or_str.decode("utf-8")
    else:
        result = bytes_or_str
    return result
