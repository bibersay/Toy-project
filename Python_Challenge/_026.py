# 20
name=input("이름 입력 :")

print(len(name))
print(name.lower())
print(name.upper())
print(name.title())

if name[0] not in ['a','e','i','o','u'] :
    print(name[1:]+name[0]+'ay')
else :
    print(name+'way')