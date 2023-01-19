import sys, os

params = {
    "version": "0.0.0",
    "increment": "patch",
    "suffix": None
}

alen = len(sys.argv)

if alen > 1:
    params['version'] = sys.argv[1]
    if alen > 2:
        params['increment'] = sys.argv[2]
        if alen > 3:
            params['suffix'] = sys.argv[3]

split = params['version'].split('.')
if params['increment'] != '':
    if params['increment'] == 'major':
        split[0] = str(int(split[0]) + 1)
        split[1] = '0'
        split[2] = '0'
    elif params['increment'] == 'minor':
        split[1] = str(int(split[1]) + 1)
        split[2] = '0'
    elif params['increment'] == 'patch':
        split[2] = str(int(split[2]) + 1)

print('.'.join(split) + (('-' + params['suffix']) if params['suffix'] not in ["", " ", None, False] else ''))