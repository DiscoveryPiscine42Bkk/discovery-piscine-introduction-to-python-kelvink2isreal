import sys

def up(arg):
    return str(arg).upper()

test = sys.argv[1]
if len(sys.argv) == 2:
    print(up(test))
else:
    print("none")
