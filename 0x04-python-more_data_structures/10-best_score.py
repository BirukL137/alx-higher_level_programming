#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        dlist = list(a_dictionary)
        largK = dlist[0]
        for i in dlist:
            if a_dictionary[largK] < a_dictionary[i]:
                largK = i
        return largK
    else:
        return
