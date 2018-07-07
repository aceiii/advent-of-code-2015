#!/usr/bin/env python
# -*- coding: utf-8 -*- 


import md5


s = "iwrupvqb"

i = 1

found = False
while not found:
    m = md5.new(s + str(i))
    h = m.hexdigest()
    if h[0:5] == "000000":
        found = True
        print("Found: " + str(i))
    else:
        i += 1
        #print(h, i)


