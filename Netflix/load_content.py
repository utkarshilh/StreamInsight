import csv 

source_file = "Netflix.csv"

target_file = "contents.csv"

default_value = 'netflix'

with open(source_file , "r", newline = '', encoding='utf-8') as source :
    reader = csv.reader(source) 
    data = list(reader)


if len(data)> 0 :

    for i in range(len(data)):
        data[i].append(default_value)


    with open(target_file, "a", newline = '', encoding='utf-8') as target:
     writer = csv.writer(target)
     writer.writerows(data) 
     open(source_file, "w").close()
     print('Data appended successfully to ' + target_file )



else :
    print("No data found in source file ")
