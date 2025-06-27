#!/usr/bin/env python3
import sys
import re

if len(sys.argv)<2:
    print("none")
else: 
    keyword = sys.argv[1]
    param = input("What was the parameter? ")
    find = (re.findall(keyword,param))
    if len(find) == 1:
        print("Good Job")
    else: 
        print("Nope, Sorry...")
    