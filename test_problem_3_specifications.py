from Problem_3 import solution1

def test_simple_cases():
    assert solution1(1000) == "1", "Error"
    assert solution1(150) == "110", "Error"
    assert solution1(147) == "1100", "Error"
    
    # Edge cases
    assert solution1(333) == "1001", "Error"
    assert solution1(963) == "10010", "Error"


# ----------- SPEC-GUIDED TESTS FOR PROBLEM 3 -----------
def test_spec_guided_zero_sum():
    # S == 0 → result must be exactly "0"
    assert solution1(0) == "0"            # sum = 0
    assert solution1(1000) == "1"         # sum = 1, ensure not "0"

def test_spec_guided_valid_binary_string():
    res = solution1(147)   # sum = 12 -> binary "1100"
    assert all(c in ('0', '1') for c in res)

def test_spec_guided_binary_value_matches_sum():
    N = 150
    S = 1 + 5 + 0
    res = solution1(N)
    assert int(res, 2) == S

def test_spec_guided_no_leading_zeros():
    N = 999
    res = solution1(N)
    assert not res.startswith("0")

def test_spec_guided_length_matches_bit_length():
    N = 147   # sum = 12 → bit_length = 4
    res = solution1(N)
    assert len(res) == 4