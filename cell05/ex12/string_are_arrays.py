#!/usr/bin/env python3
import sys
import re

if len(sys.argv) == 1:
    print("none")
else: 
    keyword = "z"
    param = sys.argv[1]
    find = re.findall(keyword,param)
    if len(find) == 0:
        print("none")
    else: 
        for x in param: #string is also an array 
           if x == 'z':
                print(f"{keyword}", end="")



