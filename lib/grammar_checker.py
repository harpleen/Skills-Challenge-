def grammar_check(text):
    if text == '':
        raise Exception('there are no words to check!')

    punctuation = ['!', '?', '.']
    new_text = text[0].upper()
    if text[0] == new_text and text[-1] in punctuation:
        return True
    else:
        return False