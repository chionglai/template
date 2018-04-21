#!/usr/bin/env python

class Math(object):
    """A math object to do some addition.

    Args:
        value (float): Dummy value. Not used.
    """

    PI = 3.141592
    """Pi constant."""

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        """float: Some dummy value."""
        return self._value

    @staticmethod
    def add(a, b):
        """Adds two numbers.

        Args:
            a (float): First number.
            b (float): Second number.

        Return:
            float: Addition of `a` and `b`
        """
        return a + b
