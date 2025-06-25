import sys
import re

if len(sys.argv) !=3:
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]
    param = re.findall(keyword,text) #re_module refindall()
    print(len(param))
