#!/usr/bin/env python

with open('ciphertext') as handle:

    content = handle.read()

    for i in range(225):
        new_string = []
        for c in content:
            new_string.append(chr((ord(c)+i)%225))

        print ("".join(new_string))