import pytest
from src import compose
# def test_compose_accepts_one_function():
#     new_func = compose.compose(str)
#     assert '5' == new_func(5)

# def test_compose_accepts_two_functions():
#     new_func = compose.compose(lambda x: x+1, str)
#     assert '6' == new_func(5)

# def test_compose_accepts_two_args():
#     new_func = compose.compose(lambda x, y: x+y, str)
#     assert '11' == new_func(5, 6)

def test_compose_accepts_one_string():
    new_func = compose.compose(lambda x: x+'a')
    assert '55a' == new_func('55')