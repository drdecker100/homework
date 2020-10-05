"""
    author: Donald
    date: Oct/05/2020 

"""

from re import findall

from math import log, log2, log10

#to take expression from user: 
print("="*70)
print("Enter mathematical expression to perfom calculation.e.g 2 + 4 ... ")
print("Or Enter x, q, exit, or quit to end operation ...")
print("="*70)

quit_options=[ 'x', 'q', 'exit', 'quit'] 

#repeat if condition remains True
while True:
    try:
        exp = input(">> ").strip().replace(" ","").replace("ln","log")

        if exp in quit_options:
            print("See you next time!!")
            break

        #to split elements in expression
        match = findall('[0-9.]+|\W|\w+\W\d+\W',exp)

        if len(match) == 1 and "log" not in exp:
            print(exp)

        #functions for addition, subtraction, multiplication, and division
        def add(x, y):
            return x + y

        def subtract(x, y):
            return x - y

        def multiply(x, y):
            return x * y

        def divide(x, y):
            return x / y

        #condition to handle single logarithms expression
        if (len(match)<3 and "log" in exp):
        
            if "log10" in exp:
                x= int(findall('\d+',exp)[1])
                print(log10(x))

            elif "log2" in exp:
                x= int(findall('\d+',exp)[1])
                print(log2(x))

            elif "log" in exp:
                x= int(findall('\d+',exp)[0])
                print(log(x))
            
        #condition to handle multiple logarithms expression
        if len(match)==3 and "log" in exp:
            num1,op,num2 = match[0],match[1],match[2]   

            if "log" in num1 and "+" == op:
                x= int(findall('\d+',exp)[0])
                print(add(log(x),float(num2)))

            elif "log" in num2 and "+" == op:
                x= int(findall('\d+',exp)[1])
                print(add(float(num1),log(x)))

            elif "log" in num1 and "-" == op:
                x= int(findall('\d+',exp)[0])
                print(subtract(log(x),float(num2)))

            elif "log" in num2 and "-" == op:
                x= int(findall('\d+',exp)[1])
                print(subtract(float(num1),log(x)))

            elif "log" in num1 and "*" == op:
                x= int(findall('\d+',exp)[0])
                print(multiply(log(x),float(num2)))

            elif "log" in num2 and "*" == op:
                x= int(findall('\d+',exp)[1])
                print(multiply(float(num1),log(x)))

            elif "log" in num1 and "/" == op:
                x= int(findall('\d+',exp)[0])
                print(divide(log(x),float(num2)))

            elif "log" in num2 and "/" == op:
                x= int(findall('\d+',exp)[1])
                print(divide(float(num1),log(x)))                

        #condition to handle multiple multiple expression with single operator
        elif len(match)==3 and "log" not in exp:

            num1,op,num2 = float(match[0]),match[1],float(match[2])

            if "+" in op:
                print(add(num1, num2))

            elif "-" in op:
                print(subtract(num1, num2))

            elif "*" in op:
                print(multiply(num1, num2))

            elif "/" in op:
                print(divide(num1, num2))
              
        #condition to handle multiple expression with double operator
        elif len(match)>3:
            num1,op1,num2,op2,num3 = float(match[0]),match[1],float(match[2]),match[3],float(match[4])

            if "+" in op1 and "+" in op2:
                print(add(add(num1, num2),num3))

            elif "+" in op1 and "-" in op2:
                print(subtract(add(num1, num2),num3))

            elif "+" in op1 and "*" in op2:
                print(multiply(add(num1, num2),num3))

            elif "+" in op1 and "/" in op2:
                print(divide(add(num1, num2),num3))
            
            
            elif "-" in op1 and "+" in op2:
                print(add(subtract(num1, num2),num3))

            elif "-" in op1 and "-" in op2:
                print(subtract(subtract(num1, num2),num3))

            elif "-" in op1 and "*" in op2:
                print(multiply(subtract(num1, num2),num3))

            elif "-" in op1 and "/" in op2:
                print(divide(subtract(num1, num2),num3))


            elif "*" in op1 and "+" in op2:
                print(add(multiply(num1, num2),num3))

            elif "*" in op1 and "-" in op2:
                print(subtract(multiply(num1, num2),num3))

            elif "*" in op1 and "*" in op2:
                print(multiply(multiply(num1, num2),num3))

            elif "*" in op1 and "/" in op2:
                print(divide(multiply(num1, num2),num3))


            elif "/" in op1 and "+" in op2:
                print(add(divide(num1, num2),num3))

            elif "/" in op1 and "-" in op2:
                print(subtract(divide(num1, num2),num3))

            elif "/" in op1 and "*" in op2:
                print(multiply(divide(num1, num2),num3))

            elif "/" in op1 and "/" in op2:
                print(divide(divide(num1, num2),num3))

    except Exception as e:
        print("Error: {}".format(e))
        print("Check input and try again")
        
