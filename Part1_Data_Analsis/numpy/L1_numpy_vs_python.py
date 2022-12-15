import numpy as np
from timeit import timeit

def py_sum(n):
    """python内置列表计算数组加法"""
    a = [i ** 2 for i in range(n)]
    b = [i ** 3 for i in range(n)]
    ab_sum = []
    for i in range(n):
        ab_sum.append(a[i] + b[i])
    return ab_sum


def np_sum(n):
    """numpy计算数组加法"""
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    return a + b


if __name__ == "__main__":
    print(py_sum(10))
    py_time=timeit("py_sum(10000)","from __main__ import py_sum",number=1000)
    print(py_time)  #py_time=7.02s
    print(np_sum(10))
    np_time=timeit("np_sum(10000)","from __main__ import np_sum",number=1000)
    print(np_time)  #np_time=0.046s