#!/usr/bin/python3
"""
Define methods to determine if a given data set represents a valid UTF-8"""

from typing import List


def to_binary(number: int) -> str:
    """converts a number to a binary string

    Args:
        number (int)

    Returns:
        str: 8 bit binary string representation of a number
        , and 8 lsb if the number is more than 8 bits long
    """
    return "{:08b}".format(number) if number < 256 \
        else "{:08b}".format(number)[-8:]


def calc_char_len(number: str) -> int:
    """count the length of a character in bytes in a utf-8 string

    Args:
        number (str): binary representation of the number to check

    Returns:
        int: the length of the utf-8 character
    """
    # if the byte starts with 0 it's a 1 byte character
    if number[0] == '0':
        return 1

    result = 0
    for bit in number:
        if bit == '0':
            break
        result += 1

    # result cannot exceed 4 in utf-8
    return result if result <= 4 else 0


def validUTF8(data: List[int]) -> bool:
    """determines if a given data set represents a valid UTF-8 encoding.
    by combining the use of
        the check_next_bytes, to_binary and calc_char_len functions

    Args:
        data (List[int]): list of int representations of chars in a utf-8
                        string.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else return False
    """

    def check_next_bytes(curr_byte_idx: int, n_bytes_to_check: int) -> bool:
        """validate the next number of bytes in the utf-8 string
            according to number of msb bits which equal 1
                returned by calc_char_len

            Example:
                the list starts with [111011100]
                this means the next 2 bytes ('1110'->
                            {3 1's - current byte count}
                should start with '10'


        Args:
            curr_byte_idx (int): _description_
            number_of_bytes_to_check (int): _description_

        """
        for i in range(curr_byte_idx + 1, curr_byte_idx + n_bytes_to_check):
            if i >= len(data) or to_binary(data[i])[:2] != '10':
                return False
        return True

    utf8_char_idx = 0
    while utf8_char_idx < len(data):
        char_bytes = calc_char_len(to_binary(data[utf8_char_idx]))
        first_byte = to_binary(data[utf8_char_idx])

        if char_bytes > 4 or char_bytes == 0:
            return False

        if char_bytes == 1:
            if first_byte[0] != '0':
                return False
            else:
                if not check_next_bytes(utf8_char_idx, char_bytes):
                    return False

        utf8_char_idx += char_bytes

    return True
