#!/usr/bin/python3
""" This module provides a function to validate UTF-8 encoding. """


def validUTF8(data):
    """Determine if a given list of integers represents a valid UTF-8 encoding.
    """
    n = len(data)
    i = 0

    while i < n:
        byte = data[i]

        if byte < 0 or byte > 255:
            return False

        if (byte & 0x80) == 0x00:
            num_bytes = 1
        elif (byte & 0xE0) == 0xC0:
            num_bytes = 2
        elif (byte & 0xF0) == 0xE0:
            num_bytes = 3
        elif (byte & 0xF8) == 0xF0:
            num_bytes = 4
        else:
            return False

        if i + num_bytes > n:
            return False

        for j in range(1, num_bytes):
            continuation = data[i + j]
            if continuation < 0 or continuation > 255:
                return False
            if (continuation & 0xC0) != 0x80:
                return False

        i += num_bytes

    return True
