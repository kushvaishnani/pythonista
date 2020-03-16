# pythonista
#Simple python program for calculator which allows you to perform single operation twice
#program is written using if-elif, if-else conditions
#I had developed this program using jupyter (take care about indentations)

print("Hi!")
x=input("enter the first number:")
y=input("enter the second number:")
xf=float(x)
yf=float(y)
print("choose the opeartor")
print("+ [Addition]")
print("- [Subtraction]")
print("* [multiplication]")
print("/ [Division]")
print("% [Modulo]")
print("** [power]")
print("== [Equal]")
z=input("enter the operator:")
if  z == '+':
    a=xf+yf
    print(a)
    print("want to perform operation again with above result?")
    further= input("yes or no:")
    if further == "yes":
        x=input("enter the number")
        print ("your final answer is:",float(a)+float(x))
    else:
        print("Your final answer is:",a)
elif z == '-':
    b=xf-yf
    print(b)
    print("want to perform operation again with above result?")
    further= input("yes or no:")
    if further == "yes":
        x=input("enter the number")
        print ("your final answer is:",float(b)-float(x))
    else:
        print("Your final answer is:",b)
elif z == '*':
    c=xf*yf
    print(c)
    print("want to perform operation again with above result?")
    further= input("yes or no:")
    if further == "yes":
        x=input("enter the number")
        print ("your final answer is:",float(c)*float(x))
    else:
        print("Your final answer is:",c)
elif z == '/':
    d=xf/yf
    print("quotient is:",d)
    print("want to perform operation again with above result?")
    further= input("yes or no:")
    if further == "yes":
        x=input("enter the number")
        print ("your final answer is:",float(d)/float(x))
    else:
        print("Your final answer is:",d)
elif z == '%':
    e=xf%yf
    print("remainder is",e)
    print("want to perform operation again with above result?")
    further= input("yes or no:")
    if further == "yes":
        x=input("enter the number")
        print ("your final answer is:",float(e)%float(x))
    else:
        print("Your final answer is:",e)
elif z == '**':
    f=xf**yf
    print(f)
    print("want to perform operation again with above result?")
    further= input("yes or no:")
    if further == "yes":
        x=input("enter the number")
        print ("your final answer is:",float(f)**float(x))
    else:
        print("Your final answer is:",f)
elif z == '==':
    if xf == yf:
            print("numbers are equal")
    else:
        print("numbers are not equal")
else:
    print("invalid opeartion")
    print("enter the valid operator")
