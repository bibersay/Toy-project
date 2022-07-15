# Stack 구현
# is empty
# is full
# push
# pop
# find
# dump
# peek
# clear
# count
# contain


class FixedStack:

    class Empty (Exception):

        pass

    class Full(Exception):

        pass

    def __init__(self, capacity):

        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self):

        return self.ptr

    def is_empty(self):

        return self.ptr <= 0

    def is_full(self):

        return self.ptr>=self.capacity

    def push(self, value):
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr +=1

    def pop(self):
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -=1
        return self.stk[self.ptr]

    def peek(self):
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr-1]

    def clear(self):
        self.ptr = 0

    def find(self, value):
        # for i in range(self.ptr-1, -1, -1):
        for s in self.stk:
            if s==value:
                return s
        return -1

    def count(self, value):
        c=0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c+=1
        return c

    def __contains__(self, value):
        return self.count(value)>0

    def dump(self):

        if self.is_empty():
            print('빈 스택')
        else :
            # print(self.stk[:self.ptr])
            print(self.stk[:self.ptr])


# [Do it! 실습 4-2] 고정 길이 스택 FixedStack의 사용하기

from enum import Enum

Menu = Enum('Menu', ['푸시', '팝', '피크', '검색', '덤프', '종료'])


def select_menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='   ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)


s = FixedStack(3)  # 최대 64개를 푸시할 수 있는 스택

while True:
    print(f'현재 데이터 개수: {len(s)} / {s.capacity}')
    menu = select_menu()  # 메뉴 선택

    if menu == Menu.푸시:  # 푸시
        x = int(input('데이터를 입력하세요.: '))
        try:
            s.push(x)
        except FixedStack.Full:
            print('스택이 가득 차 있습니다.')

    elif menu == Menu.팝:  # 팝
        try:
            x = s.pop()
            print(f'팝한 데이터는 {x}입니다.')
        except FixedStack.Empty:
            print('스택이 비어 있습니다.')

    elif menu == Menu.피크:  # 피크
        try:
            x = s.peek()
            print(f'피크한 데이터는 {x}입니다.')
        except FixedStack.Empty:
            print('스택이 비어 있습니다.')

    elif menu == Menu.검색:  # 검색
        x = int(input('검색할 값을 입력하세요.: '))
        if x in s:
            print(f'{s.count(x)}개 포함되고, 맨 앞의 위치는 {s.find(x)}입니다.')
        else:
            print('검색값을 찾을 수 없습니다.')

    elif menu == Menu.덤프:  # 덤프
        s.dump()

    else:
        break

