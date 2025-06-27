#!/usr/bin/env python3
import sys

if len(sys.argv) <=2:
    print("none")
else: 
    first = int(sys.argv[1])
    second = int(sys.argv[2])
    result = [a for a in range(first,second+1,1)] #range(start,length,interval)
    print(result)
        