#!/usr/bin/python3
"""Test unittest for class State"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """blablabla"""

    def test_args(self):
        state = State()
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
