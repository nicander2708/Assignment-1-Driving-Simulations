time = int(input('Enter the amount of time spent on the road:'))
acc = int(input('Enter the acceleration of the person:'))
distance = int(input('Enter the distance traveled:'))
v1 = 0
v= v1 + (acc*time)
d= int(time + 0.5*(acc)*(time**2))
for x in range (time + 1):
    d1 = (acc/2)*(x**2)
    print ('Duration : ',x,'Distance : ', "x"*int(d1/10))
speed_limit = 60
if v >= 60:
    print ('The person went over the speed limit. (Max speed was ', v ,'m/s.)' )
else:
    print('The person did not go over the speed limit. (Max speed was ',v, 'm/s)' )

if d >= distance:
    print('The person reached the destination. (Reached' ,d, 'm)')
else:
    print('The person did not reach the destination. (Reached',d, 'm)')

