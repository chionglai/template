#!/usr/bin/env python

import pytest
from template.dummy import Math

@pytest.mark.parametrize("value", [1, 2])
@pytest.mark.parametrize("a", [1, 2])
@pytest.mark.parametrize("b", [4, 5])
def test_math(value, a, b):
    mm = Math(value)
    assert mm.add(a, b) == a + b
