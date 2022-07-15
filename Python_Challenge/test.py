import csv
file = csv.reader(open('list.csv'))
data=[]

for f in file:
    print(f)
    data.append(f)
print(data[0][1])