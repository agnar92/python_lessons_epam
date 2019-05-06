"""
Solution for home tasks session 4.
"""

import unittest
from functools import reduce

def bold(function):
    def wrapper(string):
        value = "\033[1m"
        return function(value + string)
    return wrapper

def italic(function):
    def wrapper(string):
        value = "\033[3m"
        return function(value + string)
    return wrapper

def underline(function):
    def wrapper(string):
        value = "\033[4m"
        return function(value + string)
    return wrapper


def h_1(num_1, num_2, num_3):
    """
    Write a Python function to find the Max of three numbers.
    :param a:
    :param b:
    :param c:
    :return: max of numbers
    """
    return max(num_1, num_2, num_3)


def h_2(string):
    """
    Write a Python program to reverse a string.
    :param string:
    :return: str
    """
    return string[::-1]


def h_3(lst):
    """
    Write a Python function to sum all the numbers in a list.
    :param lst:
    :return: int
    """
    return sum(lst)


def h_4(num):
    """
    Write a Python function to calculate the factorial of a number (a non-negative integer).
    The function accepts the number as an argument.
    :param num:
    :return: int
    """
    return 1 if num == 1 else num * h_4(num - 1)


def h_5(lst):
    """
    Write a Python function to multiply all the numbers in a list.
    :param lst:
    :return: float
    """
    return reduce(lambda x, y: x * y, lst)


def h_6(string):
    """
    Write a Python function that accepts a string and calculate the number of
    upper case letters and lower case letters.
    :param string:
    :return: tuple
    """
    return sum(map(str.islower, string)), sum(map(str.isupper, string))


def h_7(lst):
    """
    Write a Python function that takes a list and returns a new list with unique
    elements of the first list.
    :param lst:
    :return: list
    """
    return list(set(lst))


def h_8(num):
    """
    Write a Python function that takes a number as a parameter and check the
    number is prime or not.
    :param num:
    :return: boolean
    """
    return bool(True for i in range(2, num // 2) if (num % i) != 0) if num > 1 else False

@bold
@italic
@underline
def h_9(string):
    """
    Write a Python program to make a chain of function decorators
    (bold, italic, underline etc.) in Python.
    :param string:
    :return:
    """
    return string


def h_10(code):
    """
    Write a Python program to execute a string containing Python code.
    :param code:
    :return: execute code
    """
    return eval(code)


def h_11(func):
    """
    Write a Python program to access a function inside a function.
    :return:
    """
    return func()



def h_12(func):
    """
    Write a Python program to detect the number of local variables declared in a function.
    :return:
    """
    return func.__code__.co_nlocals


def h_13(lst):
    """
    Write a Python program to print the even numbers from a given list.
    :param lst:
    :return: list
    """
    return [x for x in lst if x % 2 == 0]


def h_14(num):
    """
    Write a Python function to check whether a number is perfect or not.
    :param num:
    :return: boolean
    """
    positive_divisions = [x for x in range(1, num, 1) if num % x == 0]

    return (sum(positive_divisions) == num and
            (sum(positive_divisions) + num) // 2 == num)


def h_15(string):
    """
    Write a Python program that accepts a hyphen-separated sequence of words as
    input and prints the words in a hyphen-separated sequence after sorting
    them alphabetically.
    :param string:
    :return:
    """
    return "-".join(sorted(string.split("-")))


### Unit Tests ###


class Session4(unittest.TestCase):

    def test_h_1(self):
        self.assertEqual(h_1(1, 5, 2), 5, "Should be 5")

    def test_h_2(self):
        self.assertEqual(h_2("1234abcd"), "dcba4321")

    def test_h_3(self):
        self.assertEqual(h_3((8, 2, 3, 0, 7)), 20)

    def test_h_4(self):
        self.assertEqual(h_4(5), 120)

    def test_h_5(self):
        self.assertEqual(h_5((8, 2, 3, -1, 7)), -336)

    def test_h_6(self):
        self.assertEqual(h_6('The quick Brow Fox'), (12, 3))

    def test_h_7(self):
        self.assertEqual(h_7([1, 2, 3, 3, 3, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_h_8(self):
        self.assertEqual(h_8(1), False)
        self.assertEqual(h_8(11), True)

    def test_h_9(self):
        self.assertEqual(h_9('Hello'), '\033[4m\033[3m\033[1mHello')

    def test_h_10(self):
        ex = """1*2"""
        self.assertEqual(h_10(ex), 2)

    def test_h_11(self):
        def h_11_1():
            return 'Hello'
        self.assertEqual(h_11(h_11_1), 'Hello')

    def test_h_12(self):
        def h_12_1():
            numb_a = 1
            numb_b = 2
            return numb_a + numb_b

        self.assertEqual(h_12(h_12_1), 2)

    def test_h_13(self):
        self.assertEqual(h_13([1, 2, 3, 4, 5, 6, 7, 8, 9]), [2, 4, 6, 8])

    def test_h_14(self):
        self.assertEqual(h_14(496), True)
        self.assertEqual(h_14(8128), True)



if __name__ == "__main__":
    unittest.main()
