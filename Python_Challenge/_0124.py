import csv

file = csv.reader(open("books.csv"))
# a=list(file)
for i,f in enumerate(file):
    print(i,' ',f)

# print(a[2])