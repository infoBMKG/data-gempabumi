import function #impor file function.py
import json
result = json.loads(function.gempadirasakan())
for x in result:
    for y in result[x]:
        print("{:<15} : ".format(y) + result[x][y])
    print("\n")
© 2021 GitHub, Inc.
