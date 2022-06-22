import random 
import datetime

  
f = open("RandomLoadTestFile.csv","x") 

f.close() 

#row_count = os.environ['rowcount_in_fileToBeUploaded'] 

row_count = 3722568
#row_count=5

valid_itemNames = ('AHU1_RUN_COMMAND_OBS', 'AHU1_FILTER_STATUS_OBS') 

valid_qualities = ('good', 'bad') 

iter = 0 

file = open("RandomLoadTestFile.csv","a") 

startdate = "2021-11-01T01:00:00.539687Z"
dated = datetime.datetime.fromisoformat(startdate[:-1])
seconds = 5
while iter < row_count: 
    #output will be of the Format 2021-11-01 01:00:05.539687
    dated = dated + datetime.timedelta(seconds=seconds)


    #Replacing space between date and Time with T to supprt format 2021-11-01T01:00:05+00:00
    datestring=str(dated).replace(" ", "T") 

    # Replacing .539687 with +00:00 to support format 2021-11-01T01:00:05+00:00
    datestring=datestring.replace(".539687", "+00:00")

    data = datestring + ',' + random.choice(valid_itemNames) + ',' + str(round(random.uniform(3.33, 666.66), 2)) + ',' + random.choice(valid_qualities) 

    # print (data)
    file.write(data) 

    file.write("\n") 

    iter += 1 


