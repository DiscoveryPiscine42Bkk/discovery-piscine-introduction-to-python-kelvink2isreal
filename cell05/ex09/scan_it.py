import sys
import re

if len(sys.argv)!=3:
    print("none")
else: 
    keyword = sys.argv[1]
    text = sys.argv[2]
    search = re.findall(keyword,text)
    if len(search) == 0:
        print("none")
    else: 
        print(len(search))