import csv 

import os 

mid_file = 'Netflix/contents.csv'

final_file = 'compiled_contents.csv'


if os.path.exists(mid_file):
    with open(mid_file, "r" , newline = '', encoding = 'utf-8') as src :
        rows = list(csv.reader(src))
else :
    rows = []


if rows :
    with open(final_file, "a" , newline = '', encoding = 'utf-8') as tgt :
        csv.writer(tgt).writerows(rows)

        print("Data appended successfully ") 
else :
    print("No data to move ")

with open(mid_file, "w" , newline = '', encoding='utf-8') as src :
    pass 
print("Mid file cleared successfully ")







 

