def menu1(s, sol):
    if s == sol:
        return True

    a,b,c,d = s
    x,y,z,w = sol
    print(a,b,c,d)

    color=0
    pos=0
    if a in sol :
        if a ==x :
            pos +=1
        else :
            color +=1

    if b in sol :
        if b ==y :
            pos +=1
        else :
            color +=1

    if c in sol:
        if c == z:
            pos += 1
        else:
            color += 1

    if d in sol:
        if d == w:
            pos += 1
        else:
            color += 1

    print(f'correct pos : {pos}\n correct colour : {color}')
    return False


def main():
    cnt = 0
    sol = input("정답 입력 : ")
    go =True
    while go:
        print('Answer :')
        print('count? : c')
        print('quit? : q')
        print()

        selec = input("메뉴 선택 :")
        if selec == 'c':
            print(cnt)
            continue
        if selec == 'q':
            exit()

        try:
            int(selec)
            if len(selec) == 4:
                if menu1(selec, sol):
                    print('you win')
                    go=False
                    continue
                else : cnt += 1
        except:
            print("메뉴  재선택 :")
            continue


main()
