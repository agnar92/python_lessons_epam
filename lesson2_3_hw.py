# -*- coding: utf-8 -*-
"""
Solutions for Home tasks from lesson 2 and 3.
"""
import itertools


# 1
def check_empty_lst(lst):
    """
    1. Write a Python program to check if all dictionaries in a list are empty
    or not. Go to the editor
    Sample list : [{},{},{}]
    Return value : True
    Sample list : [{1,2},{},{}]
    Return value : False
    :param list:
    :return: boolean
    """
    for i in lst:
        if i:
            return True
    return False


print(check_empty_lst([{1, 2}, {}, {}]))
print(check_empty_lst([{}, {}, {}]))


# 2
def remove_duplicates_from_nested_list(lst):
    """
    2. Write a Python program to remove duplicates from a list of lists.
    Go to the editor
    Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    New List : [[10, 20], [30, 56, 25], [33], [40]]
    :param lst:
    :return: list
    """
    return [l for n, l in enumerate(lst) if l not in lst[:n]]


print(remove_duplicates_from_nested_list([[10, 20], [40], [30, 56, 25],
                                          [10, 20], [33], [40]]))


# 3
def max_from_list(lst):
    """
    3. Write a Python program to find the list in a list of lists whose sum of
    elements is the highest. Go to the editor
    Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
    Expected Output: [10, 11, 12]
    :param lst:
    :return: list
    """
    return max([(l, sum(l)) for l in lst], key=lambda x: x[1])[0]


print(max_from_list([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]))


# 4
def diff(lst1, lst2):
    """
    4. Write a Python program to compute the similarity between two lists.
    Go to the editor
    Sample data: ["red", "orange", "green", "blue", "white"],
    ["black", "yellow", "green", "blue"]
    Expected Output:
    Color1-Color2: ['white', 'orange', 'red']
    Color2-Color1: ['black', 'yellow']
    :param l1:
    :param l2:
    :return: two lists
    """
    return [c for c in lst1 if c not in lst2], [b for b in lst2 if b not in lst1]


print(diff(["red", "orange", "green", "blue", "white"],
           ["black", "yellow", "green", "blue"]))


# 5
def change_position(lst):
    """
    5. Write a Python program to change the position of every n-th value
    with the (n+1)
    th in a list. Go to the editor
    Sample list: [0,1,2,3,4,5]
    Expected Output: [1, 0, 3, 2, 5, 4]
    :param l:
    :return: list
    """
    for i in range(0, len(lst) - 1, 2):
        new_position = lst.index(lst[i]) + 1
        lst.insert(new_position, lst.pop(lst.index(lst[i])))
    return lst


change_position([0, 1, 2, 3, 4, 5])


# 6
def order_tuples(lst):
    """
    6. Write a Python program to get a list, sorted in increasing order by the
    last element in each tuple from a given list of non-empty tuples.
    Go to the editor
    Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
    :param lst:
    :return: list of ordered tuples
    """
    return sorted(lst, key=lambda x: x[1])


print(order_tuples([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


# 7
def counting(lst):
    """
    7. Write a Python program to count the number of strings where the string
    length is 2 or more and the first and last character are same from
    a given list of strings. Go to the editor
    Sample List : ['abc', 'xyz', 'aba', '1221']
    Expected Result : 2
    :param l:
    :return: int
    """
    count = 0
    for value in lst:
        if len(value) >= 2 and value[0] == value[-1]:
            count += 1

    return count


counting(['abc', 'xyz', 'aba', '1221'])

# 8
print("This is a tuple {t}".format(t=(100, 200, 300)))


# 9
def replace_in_tuple(lst, value):
    """
    9. Write a Python program to replace last value of tuples in a list.
    Go to the editor
    Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
    :param lst:
    :param value:
    :return:  list of tuples
    """
    return [t[:-1] + (value,) for t in lst]


print(replace_in_tuple([(10, 20, 40), (40, 50, 60), (70, 80, 90)], 100))


# 10
def remove_empty_tuple(lst):
    """
    10. Write a Python program to remove an empty tuple(s)
    from a list of tuples. Go to the editor
    Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
    Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
    :param lst:
    :return: list
    """
    return [l for l in lst if l]


remove_empty_tuple([(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d',)])


# 11
def order_tuples_float(lst):
    """
    11. Write a Python program to sort a tuple by its float element.
    Go to the editor
    Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
    Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
    :param lst:
    :return: sorted list of tuples
    """
    return sorted(lst, key=lambda x: x[1], reverse=True)


print(order_tuples_float([('item1', '12.20'),
                          ('item2', '15.10'),
                          ('item3', '24.5')]))


# 12
def shallow_copy(lst):
    """
    12. Write a Python program to create a shallow copy of sets.
    Go to the editor
    Note : Shallow copy is a bit-wise copy of an object. A new object is created
    that has an exact copy of the values in the original object.
    :param lst:
    :return: shallow object
    """
    return lst.copy()


print(shallow_copy([1, 2]))


# 13
def remove_set(orginal_set, el_to_del):
    """
    13. Write a Python program to remove an item
    from a set if it is present in the set.
    :param orginal_set:
    :param el_to_del:
    :return: new set
    """
    orginal_set.discard(el_to_del)
    return orginal_set


remove_set({1, 2, 3}, 3)


# 14
def unique_values(dic):
    """
    14. Write a Python program to print all unique values in a dictionary.
    Go to the editor
    Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
    {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
    Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
    :param d:
    :return:
    """
    return set(list(value.values())[0] for value in dic)


unique_values(
    [{"V": "S001"},
     {"V": "S002"},
     {"VI": "S001"},
     {"VI": "S005"},
     {"VII": "S005"},
     {"V": "S009"},
     {"VIII": "S007"}])


# 15

def create_w(dic):
    """
    15. Write a Python program to create and display all combinations of letters,
    selecting each letter from a different key in a dictionary. Go to the editor
    Sample data : {'1':['a','b'], '2':['c','d']}
    Expected Output:
    ac
    ad
    bc
    bd
    :param dic:
    :return: str
    """
    for value in itertools.product(*dic.values()):
        print(''.join(value))


create_w({'1': ['a', 'b'], '2': ['c', 'd']})


# 16
def count_words(string):
    """
    16. Write a Python program to create a dictionary from a string.
    Go to the editor
    Note: Track the count of the letters from the string.
    Sample string : 'w3resource'
    Expected output: {'3': 1,'s': 1, 'r': 2, 'u': 1,
                      'w': 1, 'c': 1, 'e': 2, 'o': 1}
    :param str:
    :return: dict
    """
    from collections import Counter
    return dict(Counter(string))


print(count_words('w3resource'))


# 17
def sort_values(dic):
    """
    17. Write a Python program to get the top three items in a shop. Go to the editor
    Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
    Expected Output:
    item4 55
    item1 45.5
    item3 41.3
    :param dic:
    :return: dict
    """
    sorted_dict = sorted(dic.items(), key=lambda t: t[1], reverse=True)
    return sorted_dict[:3]


print(sort_values({'item1': 45.50,
                   'item2': 35,
                   'item3': 41.30,
                   'item4': 55,
                   'item5': 24}))


# 18
def create_dict(lst1, lst2):
    """
    18. Write a Python program to create a dictionary from two lists without
    losing duplicate values. Go to the editor
    Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'],
                   [1, 2, 2, 3]
    Expected Output: defaultdict(<class 'set'>, {'Class-VII': {2},
    'Class-VI': {2}, 'Class-VIII': {3}, 'Class-V': {1}})
    :param l1:
    :param l2:
    :return: dict
    """
    result = dict()
    for key, value in zip(lst1, lst2):
        result[key] = value

    return result


print(create_dict(['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'],
                  [1, 2, 2, 3]))


# 19
def in_dict(dic1, dic2):
    """
    19. Write a Python program to match key values in two dictionaries.
    Go to the editor
    Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
    Expected output: key1: 1 is present in both x and y
    :param d1:
    :param d2:
    :return: None
    """
    for key, value in dic1.items():
        if value in dic2.values():
            print("{key} : {value} ins both d1 and d2".format(key=key, value=value))
        else:
            print("Only in d1")


in_dict({'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2})


# 20
def my_sum(lst):
    """
    20. Write a Python function to sum all the numbers in a list.
    Go to the editor
    Sample List : (8, 2, 3, 0, 7)
    Expected Output : 20
    :param l:
    :return: int
    """
    return sum(lst)


my_sum((8, 2, 3, 0, 7))


# 22
def sort_words(string):
    """
    22.Write a Python program that accepts a hyphen-separated sequence of words
    as input and prints the words in a hyphen-separated sequence after
    sorting them alphabetically. Go to the editor
    Sample Items : green-red-yellow-black-white
    Expected Result : black-green-red-white-yellow
    :param string:
    :return: str
    """
    return "-".join(sorted(string.split('-')))


sort_words('green-red-yellow-black-white')


# 23
def perfect_number(number):
    """
    3. Write a Python function to check whether a number is perfect or not.
    According to Wikipedia : In number theory, a perfect number is a positive
    integer that is equal to the sum of its proper positive divisors, that is,
    the sum of its positive divisors excluding the number itself
    (also known as its aliquot sum). Equivalently, a perfect number is a number
    that is half the sum of all of its positive divisors (including itself).
    Example : The first perfect number is 6, because 1, 2, and 3 are its proper
    positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to
    half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6.
    The next perfect number is 28 = 1 + 2 + 4 + 7 + 14.
    This is followed by the perfect numbers 496 and 8128.
    :param number:
    :return: boolean
    """
    positive_divisions = [x for x in range(1, number, 1) if number % x == 0]

    if sum(positive_divisions) == number and \
            (sum(positive_divisions) + number) / 2 == number:
        return True
    return False


perfect_number(496)
perfect_number(497)
perfect_number(8128)


# 24
def even_numbers(lst):
    """
    Write a Python program to print the even numbers from a given list.
    Go to the editor
    :param l:
    :return: list
    """
    return [i for i in lst if i % 2 == 0]


even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
