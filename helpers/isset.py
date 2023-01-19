import sys

if len(sys.argv) < 2 or sys.argv[2] in ["", " ", None, False, "False", "false", "FALSE", 0]:
    print("")
else:
    print(sys.argv[1])