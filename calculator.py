#
import math,sys

def add(a,b):
	return a+b

def sub(a,b):
	return math.abs(a-b)

def	mul(a,b):
	return a*b

def div(a,b):
	return a//b

def mod(a,b):
	return a%b


def calculate(n):
    if n==1:
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        print("Output:"+str(add(a,b)))
    
    elif n==2:
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        print("Output:"+str(sub(a,b)))
    
    elif n==3:
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        print("Output:"+str(mul(a,b)))
    
    elif n==4:
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        print("Output:"+str(div(a,b)))
    
    elif n==5:
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        print("Output:"+str(mod(a,b)))
    
    elif n==6:
        a=int(input("Enter number: "))
        print("Output:"+str(math.factorial(a)))

    elif n==7:
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        print("Output:"+str(math.gcd(a,b)))

    elif n==8:
        a=int(input("Enter number: "))
        print("Output:"+str(math.exp(x)))

    elif n==9:
        a=int(input("Enter number: "))
        b=int(input("Enter base: "))
        print("Output:"+str(math.log(a,b)))

    elif n==10:
        a=int(input("Enter number: "))
        print("Output: "+str(math.log2(a)))

    elif n==11:
        a=int(input("Enter number: "))
        print("Output: "+str(math.log10(a)))

    elif n==12:
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        print("Output: "+str(math.pow(a,b)))

    elif n==13:
        a=int(input("Enter number: "))
        print("Output: "+str(a**2))

    elif n==14:
        a=int(input("Enter number: "))
        print("Output: "+str(math.sqrt(a)))
    
    elif n==15:
        a=int(input("Enter angle: "))
        print("Output: "+str(math.sin(a)))

    elif n==16:
        a=int(input("Enter angle: "))
        print("Output: "+str(math.cos(a)))

    elif n==17:
        a=int(input("Enter angle: "))
        print("Output: "+str(math.tan(a)))

    elif n==18:
        a=int(input("Enter angle: "))
        print("Output: "+str(math.asin(a)))

    elif n==19:
        a=int(input("Enter angle: "))
        print("Output: "+str(math.acos(a)))

    elif n==20:
        a=int(input("Enter angle: "))
        print("Output: "+str(math.atan(a)))

    elif n==21:
        a=int(input("Enter first number: "))
        print("Output: "+str(math.sinh(a)))
    
    elif n==22:
        a=int(input("Enter angle: "))
        print("Output: "+str(math.cosh(a)))

    elif n==23:
        a=int(input("Enter angle: "))
        print("Output: "+str(math.tanh(a)))

    elif n==24:
        a=int(input("Enter angle: "))
        print("Output: "+str(math.asinh(a)))

    elif n==25:
        a=int(input("Enter angle: "))
        print("Output: "+str(math.acosh(a)))

    elif n==26:
        a=int(input("Enter angle: "))
        print("Output: "+str(math.atanh(a)))

    elif n==27:
        print("Output: "+str(math.pi))

    elif n==28:
        print("Output: "+str(math.e))

    else:
        print("Error")
 
def loop_condition():
    print("Do you want to continue? If yes, press 'Y' or press any other letter to stop")
    test=(input())
    if test.lower()=='y':
        return True
    else:
        return False    


def main():

    condition = True
    while condition:
        try:
            n=int(input("""Enter your choice:
1.  Addition
2.  Subtraction
3.  Multiplication
4.  Division
5.  Modulo
6.  Factorial
7.  GCD
8.  Exponential
9.  Log base x
10. Log base 2
11. Log base 10
12. a^b
13. a^2
14. Squareroot
15. sin(x)
16. cos(x)
17. tan(x)
18. Asin(x)
19. Acos(x)
20. Atan(x)
21. sinh(x)
22. cosh(x)
23. tanh(x)
24. Asinh(x)
25. Acosh(x)
26. Atanh(x)
27. Pie
28. Exponential\n"""))
            calculate(n)
        except:
            print("Unexpected Error: ", sys.exc_info()[0])

        condition=loop_condition()       

if __name__ == '__main__':
    main()




 #remaining .............   