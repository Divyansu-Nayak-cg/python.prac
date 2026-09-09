a=input("enter first number:")
b=input("enter second number:")
c=input("which operation you want to perform(+,-,*,/):")

if c=='+' or c=='-' or c=='*' or c=='/':

 if c=='+':
    print("addition:",int(a) + int(b))
 elif c=='-':
        print("substraction:",int(a) - int(b))
 elif c=='*':
            print("multiplication:", int(a) * int(b))
 elif c=='/':
                print("division:",int(a) / int(b))
else:
        print("pyari samajh gayi")                
            

