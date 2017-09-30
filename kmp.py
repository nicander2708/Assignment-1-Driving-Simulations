def kmp():

    inp = input().title()# input the name with all lowercase is also ok since .title() is used
    result = ''
    for x in inp.split('-'):
        result += x[0]
    print(result)

kmp()
