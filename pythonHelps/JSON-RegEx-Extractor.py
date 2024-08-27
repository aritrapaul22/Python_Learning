import json
import csv

f = open("C:/Users/H471459/Documents/Workbench/Workaround/pythonHelps/ID_Txt_Output.txt", "w")
# writer = csv.writer(f)

with open("response.json", "r") as file:
    jsonData = json.load(file)
    # print(jsonData)

for keys in jsonData["data"]["instances"]:
    print(keys["id"])
    f.writelines(keys["id"])
    f.write("\n")
    # writer.writerow(keys["id"])

f.close()
