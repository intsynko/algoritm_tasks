"""
написать функцию числа фибоначи

0+1=1
1+1=2
1+2=3
2+3=5
3+5=8
"""


def calc_fib(n):
    last=0 
    current=1
    for i in range(n):
        current, last = last + current, current
    return current
