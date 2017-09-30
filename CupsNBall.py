def cupnballs():


    cup1 = 1 #1 is the initial place where the ball is
    cup2 = 0
    cup3 = 0
    moves = (input('enter the move:').upper())
    for x in moves:
        if x == 'A':
            cup1 = cup1 ^ cup2
            cup2 = cup2 ^ cup1
            cup1 = cup1 ^ cup2
        elif x =='B':
            cup2 = cup2 ^ cup3
            cup3 = cup3 ^ cup2
            cup2 = cup2 ^ cup3
        elif x =='C':
            cup3 = cup3 ^ cup1
            cup1 = cup1 ^ cup3
            cup3 = cup3 ^ cup1
    if cup1 == 1:
        print ('1')
    elif cup2 == 1:
        print('2')
    elif cup3 == 1:
        print('3')


cupnballs()
