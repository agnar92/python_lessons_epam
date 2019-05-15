import calendar
import collections
import datetime
import os
import random
import shutil
import time


# Data Time
def h_1(year, week):
    return datetime.datetime.strptime(
        "{} {} w1".format(year, week), "%Y %W w%w").ctime()


def h_2(year):
    result = []
    for i in range(52):
        result.append(datetime.datetime.strptime(
            "{} {} 6".format(year, i), "%Y %W %w"
        ).ctime())
    return result


def h_3():
    pass


def h_4(formats, year=2019, month=1, day=1):
    case = {
        "a": datetime.date.today().ctime(),
        "b": datetime.date.today().year,
        "c": datetime.date(year, month, day).month,
        "d": datetime.date(year, month, day).isocalendar()[1],
        "e": datetime.date(year, month, day).weekday(),
        "f": datetime.date(year, month, day).timetuple().tm_yday,
        "g": datetime.date(year, month, day).timetuple().tm_mday,
        "h": datetime.date(year, month, day).timetuple().tm_wday
    }
    return case.get(formats)


def h_5(year=2019, month=1, day=1):
    return time.mktime(datetime.date(year, month, day).timetuple())


def h_6(string):
    return time.mktime(
        datetime.datetime.strptime(string, "%Y-%m-%d").timetuple())


def h_7(day_1, day_2):
    return abs(datetime.datetime.strptime(day_1, "%Y-%m-%d")
               - datetime.datetime.strptime(day_2, "%Y-%m-%d"))


def h_9(date):
    return datetime.datetime.strptime(date, "%Y-%m-%d").ctime()


def h_10(date):
    return datetime.datetime.strptime(date, "%Y-%m-%d").strftime('%s')


def h_11(day_1, day_2):
    i = int(datetime.datetime.strptime(day_1, "%Y-%m-%d").strftime('%s'))
    d = int(datetime.datetime.strptime(day_2, "%Y-%m-%d").strftime('%s'))
    return abs(i - d)


def h_12(current_date):
    return datetime.datetime.strptime(current_date, "%Y-%m-%d") - datetime.timedelta(days=5)


def h_13(time_stump):
    return datetime.datetime.fromtimestamp(time_stump)


def h_14():
    date = datetime.datetime.now()
    return (date - datetime.timedelta(days=1)).ctime(), date.ctime(), (date + datetime.timedelta(days=1)).ctime()


def h_15(date):
    return datetime.datetime.strptime("{} 00:00:00".format(date), "%Y-%m-%d %H:%M:%S")


def h_16(date):
    return list((datetime.datetime.strptime(date, "%Y-%m-%d") + datetime.timedelta(days=i)).ctime()
                for i in range(5))


def h_17(year):
    return calendar.isleap(year)


def h_18(data):
    return datetime.datetime.strptime(data, "%b %d %Y %I:%M%p")


def h_19():
    return datetime.datetime.today().time()


def h_20(second):
    print(datetime.datetime.today().time())
    return (datetime.datetime.today() + datetime.timedelta(seconds=second)).time()


# I/0
def list_to_file(lst):
    with open("test.txt", "w") as file:
        file.write(
            "".join(str(lst))
        )


def from_file_to_file(file_1, file_2):
    shutil.copyfile(file_1, file_2)


def combine(file_1, file_2):
    with open(file_1, 'r') as f_1, open(file_2, 'r') as f_2:
        f_3 = open("test3.txt", 'aw+')
        f_3.truncate(0)
        while True:
            l_1 = f_1.readline()
            l_2 = f_2.readline()
            f_3.write(" ".join([l_1, l_2]))
            if l_1 == '' and l_2 == '':
                break
        f_3.close()


def read_random(f_1):
    with open(f_1, 'r') as f:
        return random.choice(list(f))


def read_whole(f_1):
    with open(f_1, 'r') as f:
        return f.read()


def read_n_lines(f_1, n):
    with open(f_1, 'r') as f:
        return [f.readline() for i in range(n)]


def append_to_file(f_1, text):
    with open(f_1, 'aw') as f:
        f.write(text)
        print(f.read())


def last_n_line(f_1, n):
    with open(f_1, 'r') as f:
        lines = f.readlines()[::-1]
        return lines[:n]


def read_to_list(f_1):
    with open(f_1, 'r') as f:
        return f.readlines()


def read_lines_to_var(f_1):
    tmp = ""
    with open(f_1, 'r') as f:
        for line in f.read():
            tmp += line
    return tmp


def read_lines_to_var(f_1):
    tmp = []
    with open(f_1, 'r') as f:
        for line in f.read():
            tmp.append(tmp)
    return tmp


def longest_word(f_1):
    with open(f_1, 'r') as f:
        return sorted([{len(line): line} for line in f],
                      key=lambda x: x.keys())[-1].values()[0]


def count_lines(f_1):
    with open(f_1, 'r') as f:
        return len(f.readlines())


def frequency(f_1):
    with open(f_1, 'r') as f:
        return collections.Counter(f.readlines())


def size_of_file(f_1):
    return os.stat(f_1).st_size


def check_state_of_file(open_file):
    print(open_file.closed)


def remove_newlines(f_1):
    with open(f_1, 'r') as f:
        lines = f.readlines()
    return [line.rsplit('\n') for line in lines]


# exceptions

def run_time_exception():
    try:
        raise RuntimeError
    except Exception as e:
        print(e)


def divided_by_zero():
    try:
        5 / 0
    except ZeroDivisionError as e:
        print(e)


class MessageException(Exception):

    def __str__(self):
        return "Message is bad"


def test_message():
    try:
        raise MessageException
    except Exception as e:
        print(e)
