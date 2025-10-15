import pytest
from lib.reading_timer import *

"""
Given a text of 200 words 
It will return a reading time of 1.0
"""

def test_200_words_estimate():
    text = ' '.join(['word' for i in range(0,200)])
    result = reading_timer(text)

    assert result == 1.0

"""
Given a text of 400 words 
It will return a reading time of 2.0
"""

def test_400_words_estimate():
    text = ' '.join(['word' for i in range(0,400)])
    result = reading_timer(text)
    assert result == 2.0

"""
Given a text of 300 words 
It will return a reading time of 1.5
"""

def test_300_words_estimate():
    text = ' '.join(['word' for i in range(0,300)])
    result = reading_timer(text)
    assert result == 1.5

"""
Given an empty text
It will raise an exception
"""
def test_empty_string():
    with pytest.raises(Exception) as e:
        reading_timer(' ')
    error_message = str(e.value)
    assert error_message == 'There are no words to read!'
        