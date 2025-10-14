from lib.diary import *


def test_make_snippet():
    string = 'I will go to bed at 11pm'
    result = make_snippet(string)
    expected = 'I will go to bed ...'
    assert expected == result
