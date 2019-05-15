import time
import cProfile

from line_profiler import LineProfiler

def take_one_minute():
    time.sleep(58)
    return sum(map(lambda i: i/1000 , [x for x in range(10000000)]))

def using_time(fun):
    start = time.time()
    fun()
    finish = time.time()

    return finish - start

def  using_cprofile(fun):
    pr = cProfile.Profile()
    pr.enable()
    fun()
    pr.disable()
    pr.print_stats()


def main():
    # time
    print(using_time(take_one_minute))
    # cPlofile
    using_cprofile(take_one_minute)
    # line_profiler
    profile = LineProfiler()
    profile_wrapper = profile(take_one_minute)
    profile_wrapper()
    profile.print_stats()


if __name__ == "__main__":
    main()