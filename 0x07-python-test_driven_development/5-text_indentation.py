#!/usr/bin/python3
"""text_indentation."""


def text_indentation(text):
    """text_indentation.
    Args:
        param text: the text to be idented.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = text[:]
    for delim in ".?:":
        list_text = new_text.split(delim)
        new_text = ""
        for sent in list_text:
            sent = sent.strip(" ")
            if new_text == "":
                new_text = sent + delim
            else:
                new_text = new_text + "\n\n" + sent + delim
    print(new_text[:-3], end="")
