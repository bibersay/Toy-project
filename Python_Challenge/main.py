import csv


def menu1():
    id = input("ID :  ").lower()
    file = list(csv.reader(open('list.csv','a+')))
    table = []
    for f in file:
        table.append(f)

    for t in table:

        if id in t:
            print('already exist')
            print('retry')
            return
    pw = input("PW :  ")

    file = open('list.csv', 'a')
    newrecord = id +', '+ pw+"\n"
    file.write(str(newrecord))
    file.close()

def menu2():

    reader = csv.reader(open('list.csv','r'))
    id = input("ID :")
    write = []
    for row in reader:
        if row[0] == id:
            pw = input("PW :")
            row[1]=pw
            row = id + ', '+pw+'\n'
        write.append(row)
    w = csv.writer(open('list.csv', 'w'))
    w.writerow(write)
    print("ID 없음")


def menu3():

    reader = csv.reader(open('list.csv','r'))
    table = []
    for r in reader:
        # print(r)
        print(f'ID: {r[0]}, PW : {r[1]}')
    # file.close()

def main():
    go = True
    while go:
        print('1) create a new user ID :')
        print('2) Change a password')
        print('3) Display all user ID')
        print('4) Quit')
        print()

        selec = input("메뉴 선택 :")
        if selec == '1':
            menu1()
            continue

        if selec == '2':
            menu2()
            continue

        if selec == '3':
            menu3()
            continue

        if selec == '4':
            go = False
            continue


main()
