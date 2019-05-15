from enum import Enum
from collections import Counter, defaultdict, OrderedDict
from array import array
import heapq
import bisect
import queue


class Members(Enum):
    """
    Enum
    """
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    India = 355
    USA = 213

CLASSES = (
    ('V', 1),
    ('VI', 1),
    ('V', 2),
    ('VI', 2),
    ('VI', 3),
    ('VII', 1),
)
SEQ = [('v', 1), ('vi', 2), ('v', 3), ('vi', 4), ('vii', 1)]

def display(data):
    """
    Write a Python program to create an Enum object and display a member name
    and value.
    :param data:
    :return:
    """
    return "\nMember name: {} \n Member value: {}\n".format(data.name, data.value)


def iterate(data):
    """
    Write a Python program to iterate over an enum class and display individual
    member and their value.
    :param data:
    :return:
    """
    result = "s"
    for item in data:
        result += '{:15} = {}'.format(item.name, item.value)
    return result

def name_order_by_value(data):
    """
    Write a Python program to display all the member name of an enum class
    ordered by their values.
    :param data:
    :return:
    """
    return("\nCountry Name ordered by Country Code:\n"
           +'\n'.join(c.name for c in sorted(data, key=lambda x: x.value)))

def get_values(data):
    """
    Write a Python program to get all values from an enum class.
    :param data:
    :return:
    """
    return [item.value for item in data]

def common_words(lst):
    """
    Write a Python program to count the most common words in a dictionary.
    :param lst:
    :return:
    """
    return Counter(lst).most_common(4)

def class_roll(data):
    """
    Write a Python program to find the class wise roll number from a tuple-of-tuples.
    :param data:
    :return:
    """
    d_d = defaultdict(list)
    for name, name_id in data:
        d_d[name].append(name_id)
    return d_d

def count_words(data):
    """
    Write a Python program to count the number of students of individual class.
    :param data:
    :return:
    """
    return Counter(map(lambda x: x[0], data))

def reversed_dict(data):
    """
    Write a Python program to create an instance of an OrderedDict using a given
    dictionary. Sort the dictionary during the creation and print the members of
    the dictionary in reverse order.
    :param data:
    :return:
    """
    return reversed(OrderedDict({item.name: item.value for item in data}).items())

def sequence_dict(data):
    """
    Write a Python program to group a sequence of key-value pairs into a
    dictionary of lists.
    :param data:
    :return:
    """
    d = defaultdict(list)
    for k, v in data:
        d[k].append(v)
    return sorted(d.items())

def compere_list(lst1, lst2):
    """
    Write a Python program to compare two unordered lists (not sets).
    :param lst1:
    :param lst2:
    :return:
    """
    return Counter(lst1) == Counter(lst2)

def create_array(lst):
    """
    Write a Python program to create an array contains six integers. Also print
    all the members of the array.
    :param lst:
    :return:
    """
    aa = array('i', lst)
    for i in aa:
        print(i)
    return aa

def array_size(lst):
    """
    Write a Python program to get the array size of types unsigned integer
    and float.
    :param lst:
    :return:
    """
    aI = array('I', lst)
    af = array('f', lst)
    return aI.itemsize, af.itemsize

def array_buffer(lst):
    """
    Write a Python program to get an array buffer information.
    :param lst:
    :return:
    """
    return array('i', lst).buffer_info()

def array_length(lst):
    """
    Write a Python program to get the length of an array.
    :param lst:
    :return:
    """
    return array('i', lst).buffer_info()[1]

def convert_to_list(lst):
    """
    Write a Python program to convert an array to an ordinary list with the
    same items.
    :param lst:
    :return:
    """
    return [x for x in array('b', lst)]

def convert_to_byte(lst):
    """
    Write a Python program to convert an array to an array of machine values and
    return the bytes representation.
    :param lst:
    :return:
    """
    return array('b', lst).tobytes()

def from_to_bytes(lst):
    """
    Write a Python program to read a string and interpreting the string as an
    array of machine values.
    :param lst:
    :return:
    """
    array1 = array('i', lst)
    as_byte = array1.tobytes()
    return array('i').frombytes(as_byte)

def heap_push(data, item):
    """
    Write a Python program to push three items into the heap and print the items
    from the heap.
    :param data:
    :param item:
    :return:
    """
    return heapq.heappush(data, item)

def heap_smallest(data):
    """
    Write a Python program to push three items into a heap and return the
    smallest item from the heap. Also Pop and return the smallest item
    from the heap.
    :param data:
    :return:
    """
    return data[0], heapq.heappop(data)

def heap_pop_push(data, item):
    """
    Write a Python program to push an item on the heap, then pop and return
    the smallest item from the heap.
    :param data:
    :param item:
    :return:
    """
    return heapq.heappushpop(data, item)

def heapsort(lst):
    """
    Write a Python program to create a heapsort, pushing all values onto a heap
    and then popping off the smallest values one at a time.
    :param lst:
    :return:
    """
    heap = []
    for value in lst:
        heapq.heappush(heap, value)

    return [heapq.heappop(heap) for i in range(len(heap))]

def h_23(heap):
    """
    Write a Python program to get the two largest and three smallest items
    from a dataset.
    :param heap:
    :return:
    """
    return heapq.nlargest(2, heap), heapq.nsmallest(3, heap)

def left_insert_point(lst, x):
    """
    Write a Python program to locate the left insertion point for a
    specified value in sorted order.
    :param lst:
    :param x:
    :return:
    """
    return bisect.bisect_left(lst, x)

def right_insert_point(lst, x):
    """
    Write a Python program to locate the right insertion point for a
    specified value in sorted order.
    :param lst:
    :param x:
    :return:
    """
    return bisect.bisect_right(lst, x)

def insert_sorted(lst):
    """
    Write a Python program to insert items into a list in sorted order.
    :param lst:
    :return:
    """
    sorted_list = []
    for i in lst:
        bisect.insort(sorted_list, i)
    return sorted_list

def create_queue(n):
    """
    Write a Python program to create a queue and display all the members and size
    of the queue.
    :param n:
    :return:
    """
    q = queue.Queue()
    for x in range(n):
        q.put(x)
    return [i for i in list(q.queue)], q.qsize()

def empty_queue(q):
    """
    Write a Python program to find whether a queue is empty or not.
    :param q:
    :return:
    """
    return q.empty()

def fifo_queue(n):
    """
    Write a Python program to create a FIFO queue.
    :param n:
    :return:
    """
    q = queue.Queue()
    for i in range(n):
        q.put(i)
    return q

def lifo_queue(n):
    """
    Write a Python program to create a LIFO queue.
    :param n:
    :return:
    """
    q = queue.LifoQueue()
    for i in range(n):
        q.put(i)
    return q