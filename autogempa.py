import function #impor file function.py
import json
result = json.loads(function.autogempa())
mapURL = result["Shakemap"]
result.pop("Shakemap")
print("")
for x in result:
    print("{:<15} : ".format(x) + result[x])

print("{:<15} :".format("Shakemap"))
import IPython
IPython.display.Image(mapURL)
