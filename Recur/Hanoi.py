
n = int(input())

def hanoi(n, fr, to, tp):

    if n ==1 :
        print(f'[{n}] 을 {fr} -> {to}')
        return

    else :
        hanoi(n-1, fr,tp,to)
        print(f'[{n}] 을 {fr} -> {to}')
        hanoi(n-1, tp,to,fr)
    return

fr = '1'
to = '3'
tp ='2'
hanoi(n,fr,to,tp)