from ciscobitswap import bit_swap


def test_dcc():
    assert 2143 == bit_swap(1234)
