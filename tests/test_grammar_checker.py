import pytest
from lib.grammar_checker import *

"""
Given a text that has a capital and proper punctuation  
It will return True
"""

def test_grammar_checker():
    text = 'Hello World!'
    result = grammar_check(text)
    assert result == True

"""
Given a text that has only a capital at the beginning
It will return False
"""
def test_text_capital_only():
    text = 'Hello world'
    result = grammar_check(text)
    assert result == False

"""
Given a text that only has the punctuation at the end
It will return False
"""
def test_text_punctuation_only():
    text = 'hello world!'
    result = grammar_check(text)
    assert result == False

"""
Given an empty text
It will raise an exception
"""
def test_empty_string():
    text = ''
    with pytest.raises(Exception) as e:
        grammar_check(text)
    error_message = str(e.value)
    assert error_message == 'there are no words to check!'


"""
Given a text that only has nothing
It will return False
"""
def test_text_only():
    text = 'hello world'
    result = grammar_check(text)
    assert result == False
