import sys, os, tempfile

if os.path.isfile(sys.argv[1]):
    with open(sys.argv[1], "r") as f:
        content = f.read()
else:
    content = sys.argv[1]
path = os.path.join(tempfile.gettempdir(), 'tmp-release-file.md')

with open(path, 'w') as f:
    f.write(content)

print(path)