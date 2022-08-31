#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keylist = []
    if value in a_dictionary.values():
        for key, val in a_dictionary.items():
            if value == val:
                keylist.append(key)

        for k1 in  keylist:
            if k1 in a_dictionary:
                del a_dictionary[k1]
    return a_dictionary
