"""
Find the largest element in the array
"""

from typing import List
from math import inf


def largest_element_in_array(arr: List[int]):
    mx = -inf
    for num in arr:
        if num > mx:
            mx = num
        print(mx, num)
    print("testcase")
    return mx


test_arrays = [
    [1, 2, 3, 4, 5],
    [-10, -3, -1, -7],
    [100],
    [0, 0, 0, 0],
    [5, 3, 9, 1, 9, 2],
]
for arr in test_arrays:
    print(f"Array: {arr} -> Largest: {largest_element_in_array(arr)}")
