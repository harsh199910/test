string=input("enter a string")
if string==string[::-1]:
    print(string," is a palindrome")
else:
    print(string," is not palindrome")
if len(string)%2==0:
    print("length of string is even ",len(string))
else:
    print("length of string is odd ",len(string))
