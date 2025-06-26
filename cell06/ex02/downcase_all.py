import sys

if len(sys.argv) <= 1:
    print("none")
else:
    def down(argv):
        return str(argv).lower()
    new = sys.argv[1:]
    for i in new:
        print(down(i))
