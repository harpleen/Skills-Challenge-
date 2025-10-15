def reading_timer(text):
    if text == ' ':
        raise Exception('There are no words to read!')
    
    words = text.split()
    length_words = len(words)
    return float(length_words/200)