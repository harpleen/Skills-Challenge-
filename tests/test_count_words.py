from lib.count_words import *

def test_count_words():
    string = 'I like to eat pasta and watch tv'
    string_list = string.split()
    length_string_list = len(string_list)
    result = count_words(string)
    assert length_string_list == result