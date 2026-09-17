import unittest

from main import greet


class TestGreet(unittest.TestCase):
    def test_greet_artur(self) -> None:
        self.assertEqual(greet("Artur"), "Привет, Artur!")
