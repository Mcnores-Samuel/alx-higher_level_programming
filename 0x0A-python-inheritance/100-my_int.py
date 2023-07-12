#!/usr/bin/python3
"""This module defines MyInt class"""


class MyInt(int):
    """Defines MyInt class which inverts the == and != operators"""
    def __ne__(self, value):
        """Return the opposite if obj != value return True in place False"""
        return (super().__eq__(value))

    def __eq__(self, value):
        """Return the opposite if obj == value return False in place True"""
        return (not super().__eq__(value))
