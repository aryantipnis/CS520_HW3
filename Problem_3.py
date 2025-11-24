"""
Problem 3 - From HumanEval/84: 

Given a positive integer N, return the total sum of its digits in binary.  
Example: 
For N = 1000, the sum of digits will be 1 the output should be "1". 

For N = 150, the sum of digits will be 6 the output should be "110". 

For N = 147, the sum of digits will be 12 the output should be "1100".  

Variables: @N integer 
Constraints: 0 ≤ N ≤ 10000. 
Output: a string of binary number. 
"""

def solution1(N):
    if not isinstance(N, int):
        raise TypeError("N must be an integer")
    if N < 0:
        raise ValueError("N must be non-negative")
    
    total = 0
    n = N
    if n == 0:
        total = 0
    else:
        while n > 0:
            total += n % 10
            n //= 10
    
    return format(total, 'b')

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
S = sum(int(d) for d in str(N))

assert all(c in ('0', '1') for c in res)
assert int(res, 2) == S
assert (S == 0) == (res == "0")
assert (S > 0) == (not res.startswith("0"))
assert len(res) == (1 if S == 0 else S.bit_length())
'''

