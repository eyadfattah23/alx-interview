#!/usr/bin/python3
"""
Define methods to determine if a given data set represents a valid UTF-8"""

from typing import List


def to_binary(number: int) -> str:
    """converts a decimal integer into a binary string

    Args:
        number (int): number to convert

    Returns:
        str: binary representation of the given number
    """
    return "{:08b}".format(number)


def count_char_bytes(number: str) -> int:
    """counts the bytes of the utf char in the given binary number
        where a 1 byte char starts with '0' or '10'

    Args:
        number (str): binary representation of the char

    Returns:
        int: msb 1's bits or 1 for 1 byte characters
    """

    if len(number) > 8:
        return 0
    if number[0] == '0':
        return 1

    result = 0
    for i in number:
        if i == '0':
            break
        result += 1
    return result if result <= 4 else 0


def validUTF8(data: List[int]) -> bool:
    """check the validity of a UTF8 string

    Args:
        data (List[int]): utf8 string representation in numbers list

    Returns:
        bool: True if the list is a valid UTF8 string
            else False
    """
    if not data:
        return False

    def check_next_bytes(curr_char_idx: int, n_bytes: int) -> bool:
        """check the validity of the next number of bytes of the
            utf8 char known by it's index supposing it's not a 1 byte char.

        Args:
            curr_char_idx (int): idx of the char int he utf8 numbers/chars list
            n_bytes (int): number of bytes returned by count_char_bytes
                that defines the length of this char

        Returns:
            bool: True if the char in data[curr_char_idx] is a valid utf8
                otherwise false
        """

        for i in range(curr_char_idx + 1, curr_char_idx + n_bytes):
            if i >= len(data) or to_binary(data[i])[:2] != '10':
                return False
        return True

    utf8_byte_idx = 0
    while utf8_byte_idx < len(data):
        char_bytes = count_char_bytes(to_binary(data[utf8_byte_idx]))

        if char_bytes > 4 or char_bytes == 0:
            return False

        if char_bytes > 1 and not check_next_bytes(utf8_byte_idx, char_bytes):
            return False

        elif char_bytes == 1:
            if to_binary(data[utf8_byte_idx])[0] == '0':
                utf8_byte_idx += char_bytes
                continue
            else:
                return False

        utf8_byte_idx += char_bytes

    return True
