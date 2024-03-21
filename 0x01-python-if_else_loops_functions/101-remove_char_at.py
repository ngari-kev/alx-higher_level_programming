#!/usr/bin/python3
def remove_char_at(str, n):
    """Replaces a character at specified location (n)"""
    if n < 0 or n >= len(str):
        return str
    return ''.join([char for i, char in enumerate(str) if i != n])
