x = input('enter a string: ')
a = x[::-1]
if x == a:
    print('Pallindrome')
else:
    print('Not Pallindrome')    
z = len(x)
if z % 2 == 0:
    print('String length is even')
else:
    print('String length is odd')        