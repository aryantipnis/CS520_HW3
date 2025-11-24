"""
Problem 9 - From CodeScore-MBPP-ET:
Write a function to find t-nth term of geometric series.

"""

import math

def solution1(a, t, r):
    if not isinstance(t, int):
        raise TypeError("t must be an integer (1-based index)")
    if t < 1:
        raise ValueError("t must be >= 1")
    return a * (math.pow(r, t - 1))

'''
Problem description: <insert here>
Method signature: <insert here>

Please generate formal specifications written as assertion statements that describe the correct behavior of this method.

Requirements:
- Let 'res' denote the expected return value of the method.
- DO NOT call the method itself in the assertions (no self-reference).
- DO NOT use any side-effecting operations, including modifying data structures, I/O, randomness, or timing.
- Use only pure logic, arithmetic, boolean expressions, set membership, and comparisons.
- Provide around 5 distinct assertions unless the method allows fewer.

'''

## Generated Output: 

'''
assert isinstance(t, int) and t >= 1
assert res == a * (r ** (t - 1))
assert (t == 1) == (res == a)
assert (r == 1) == (res == a)
assert (a == 0) == (res == 0)
'''
