#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print("none")
else: 
    new_argv = sys.argv[1:]
    for x in reversed(new_argv): # for x in reversed ()
        print(x)
