import unittest
import itertools

from python_template_repo import multiply


def test_multiply():
    for i, j in itertools.product(range(100), range(100)):
        assert i * j == multiply(i, j)
