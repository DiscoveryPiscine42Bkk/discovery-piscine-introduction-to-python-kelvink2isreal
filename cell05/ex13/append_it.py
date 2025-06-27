#!/usr/bin/env python3
import sys

if len(sys.argv)<= 1:
    print("none")
else: 
    x = sys.argv[1:]
    for a in x:
        if a.endswith("ism"):
            continue
        else:
            print(a+"ism")

