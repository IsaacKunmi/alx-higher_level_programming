#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return tuple([0, None])
    else:
        length = len(sentence)
        first_sentence = sentence[0]
        tuple_list = length, first_sentence
        return tuple_list
