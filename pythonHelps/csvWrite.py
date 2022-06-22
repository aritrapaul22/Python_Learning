import csv
import datetime
import json
import random

seconds = 5  # Parameter to increment seconds
asset_start = 0
asset_end = 75
pointid_start = 1  # Pointid start time
pointid_end = 100000  # pointid end time
count = 0
# flag = True
# date = "2017-07-05T08:17:28+05:30"
dated = "2021-06-01T01:00:00.539687Z"
dated = datetime.datetime.fromisoformat(dated[:-1])
fields = ['good', 'bad']
date = "2021-06-01T01:00:00.539687Z"

employee_writer = open('Parser_75lac_70000.csv', mode='w')

for i in range(asset_start, asset_end):
    assetName = "asset" + str(i)
    for j in range(pointid_start, pointid_end):
        dated = dated + datetime.timedelta(seconds=seconds)
        # print(dated)
        count += 1
        pointId = "point" + str(j)
        data = {
            "Times": str(dated),
            "ItemName": pointId,
            "SequenceId": random.randint(15, 200),
            "assetNameId": random.choice(fields)
        }

        l1 = list(data.values())  # modifying data in to list
        s1 = str(l1)  # list to str conversion
        s1 = s1.strip("[']")  # ['2021-06-01T01:00:00.539687Z', 'point5', 32, 'bad']
        s1 = s1.replace("'", "")  # 2021-06-01T01:00:00.539687Z', 'point4', 31, 'good
        s1 = s1.replace(" ", "T")
        s1 = s1.replace(",T", ",")
        s1 = s1.replace(".539687", "+05:30")
        print(s1)
        employee_writer.write((str(s1)))
        employee_writer.write('\n')
    # data1 = json.dumps(data) #json conversion
    # employee_writer.write(str(data1))
    # employee_writer.write('\n')
    # print(data1)
