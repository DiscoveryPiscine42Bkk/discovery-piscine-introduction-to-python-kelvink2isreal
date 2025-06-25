import sys

if len(sys.argv) == 1:
    print("none")
else:
    arg = sys.argv[1:]
    print(f"parameters: {len(arg)}")
    for x in arg:
        pos = len(x)
        print(x, end = f": {pos}")
        print()
