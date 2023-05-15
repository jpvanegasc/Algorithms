"""
Bubble Sort implementation
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def bubble_sort(lis):
    sorted_lis = lis
    L = len(lis)

    while L > 0:
        L -= 1
        for i in range(L):
            if sorted_lis[i] > sorted_lis[i + 1]:
                big = sorted_lis[i]
                small = sorted_lis[i + 1]

                sorted_lis[i] = small
                sorted_lis[i + 1] = big

    return sorted_lis


if __name__ == "__main__":
    from random import randint

    mylis = [randint(0, 100) for i in range(1000)]
    print(bubble_sort(mylis))
