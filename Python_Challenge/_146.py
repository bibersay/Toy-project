
def menu1(s):

    S=[]
    for i in range(len(s)):
        if s[i] =='z':
            S.append(' ')
            continue
        S.append(chr(ord(s[i])+1))
    print(S)
    return

def menu2(s):
    S = []
    for i in range(len(s)):
        if s[i] == ' ':
            S.append('z')
            continue
        S.append(chr(ord(s[i]) - 1))
    print(S)

def menu3():
    exit()

def main():

    while True:
        print('1) Make a code')
        print('2) Decode a message')
        print('3) Quit')
        print()

        selec=input("메뉴 선택 :")
        if selec == '1':
            text = input("문자 입력:")
            menu1(text)
        elif selec =='2':
            menu2(text)
        elif selec=='3' :
            menu3()

        else:
            selec = input("메뉴  재선택 :")

main()