import itertools
import math

class ConvertToRoman:
    """
    Write a Python class to convert an integer to a roman numeral.
    """
    INT_TO_ROMAN = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
        }

    def __init__(self, number):
        self._number = number

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value


    def convert(self):
        result = []
        for k, v in ConvertToRoman.INT_TO_ROMAN.items()[::-1]:
            count = self.number // k
            self.number -= count * k
            result.append(v * count)

        return "".join(result)


class ConvertToInt:
    Roman_TO_INT = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 40,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def __init__(self, number):
        self._string = number

    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, value):
        self._string = value

    def convert(self):
        result = 0
        lst = [ConvertToInt.Roman_TO_INT.get(c) for c in self.string]
        for i in range(len(lst)):
            if i > 0 and lst[i] > lst[i-1]:
                result += lst[i] - 2 * lst[i-1]
            else:
                result += lst[i]
        return result
        # return reduce(lambda x, y: +x if x >= y else -x, lst)

class ValidityOfBrackets:

    def __init__(self, string):
        self.__opening = tuple('({[')
        self.__closing = tuple(')}]')
        self.__maping = dict(zip(self.__opening, self.__closing))
        self.__queue = []
        self.__string = string

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, value):
        self.__string = value


    def check(self):
        if len(self.string) % 2 != 0:
            return False

        for l in self.string:
            if l in self.__opening:
                self.__queue.append(self.__maping[l])
            elif l in self.__closing:
                if not self.__queue or l != self.__queue.pop():
                    return False
        return not self.__queue


class Subsetes:

    def __init__(self, array):
        self.__array = array

    @property
    def array(self):
        return self.__array

    @array.setter
    def array(self, value):
        self.__array = value

    def geneate(self):
        return list(itertools.chain.from_iterable(
            itertools.combinations(self.array, i) for i in range(len(self.array)+1)))

class Zero:

    def __init__(self, array):
        self.__array = array

    @property
    def array(self):
        return self.__array

    @array.setter
    def array(self, value):
        self.__array = value


    def check(self):
        return [tup for tup in itertools.combinations(self.array, 3)
                if sum(tup) == 0]

class Power:

    def __init__(self, number, n):
        self.__number = number
        self.__n = n

    def __repr__(self):
        return "{}".format(self.__count())

    @property
    def number(self):
        return self.__number

    @property
    def n(self):
        return self.__n

    @number.setter
    def number(self, value):
        self.__number = value

    @n.setter
    def n(self, value):
        self.__n = value

    def __count(self):
        return reduce(lambda x,y: x*y, [self.number for _ in range(self.n)])

class Revers:

    def __init__(self, string):
        self.string = string

    def rev(self):
        return " ".join([
            x for x in self.string.split(" ")[::-1]
        ])

class String:

    def __init__(self):
        self.__string = None

    def get_String(self, string):
        self.__string = string

    def pritn_String(self):
        print(self.__string.upper())

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * pow(self.radius, 2)

    def perimeter(self):
        return 2 * math.pi * self.radius
