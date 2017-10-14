inp = int(input())
for x in range(0,int(inp)):
    a,b = map(int,input().split())
    if a < b:
        print('<')
    elif a > b:
        print('>')
    elif a == b:
        print('=')

