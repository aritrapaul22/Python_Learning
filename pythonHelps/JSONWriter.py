import json
import random
import time
from datetime import datetime

DevStart = 70100
DevEnd = 70199
itn = 96
count = 0

for item in range(DevStart, DevEnd):
    with open(f"C:/Users/H471459/Documents/Workbench/IOT Platform/PI22.2/JSON Blob/ProfilerTestFile_20MB/FielUpload_{itn}k_{item}.json", "w") as file:
        file.write("[")
        for i in range(itn):
            for j in range(1, 1000):
                file.writelines(f'{{\"Properties\":{{\"Temprature\":\"{random.randint(10,90)}.9\",\"Condition\":\"Good\",\"Point\":\"In-Transit\"}},\"Time\":\"{datetime.now().isoformat()}+05:30\",\"ItemName\":\"point{j}\",\"Value\":{random.random()},\"Quality\":{random.randint(1,5)}}},')
                count += 1
                time.sleep(0.1)

        file.write("]")
        print(f"{count} Rows written.")
