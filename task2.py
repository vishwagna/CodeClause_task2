def add(a,b):
    sum=(a+b)
    return sum
def sub(a,b):
    diff=(a-b)
    return diff
def mul(a,b):
    prod=a*b
    return prod
def div(a,b):
    quo=a/b
    return quo
def exp(b,p):
    res=pow(b,p)
    return res
def sq(a):
    res=pow(a,2)
    return res
option= input('''Enter your choice: 
1.Sum
2.Difference
3.Product
4.Quotient
5.Square
6.Exponent  
''')
if(option=='1'):
   try:
      a= float(input("Enter first number "))
      b= float(input("Enter second number "))      
   except ValueError:
       print("Enter integer values only!!")
   else:
      print("Result:")
      print(add(a,b))
elif(option=='2'):
   try:
      a= float(input("Enter first number "))
      b= float(input("Enter second number "))      
   except ValueError:
       print("Enter integer values only!!")
   else:
        print("Result:")
        print(sub(a,b))
elif(option=='3'):
   try:
      a= float(input("Enter first number "))
      b= float(input("Enter second number "))      
   except ValueError:
       print("Enter integer values only!!")
   else:
        print("Result:")
        print(mul(a,b))
elif(option=='4'):
   try:
      a= float(input("Enter first number "))
      b= float(input("Enter second number "))      
   except ValueError:
       print("Enter integer values only!!")
   except ZeroDivisionError:
       print("You cant divide by 0.Try to run again!")
   else:
        print("Result:")
        print(div(a,b))
elif(option=='5'):
    try:
        a=int(input("enter a number: "))
    except ValueError:
        print("Enter integer values only!!")
    else:
        print("Result:")
        print(sq(a))
elif(option=='6'):
    try:
        b=int(input("Enter base "))
        p=int(input("Enter exponent "))
        if(p < 0):
                print("You cant enter negative integers as Power.Try to run again!")
        else:
                print("Result:")
                print(exp(b,p))
    except ValueError:
        print("Enter integer values only!!")
else:
    print(0)