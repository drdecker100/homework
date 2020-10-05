"""
Created on Mon Oct  5 09:22:35 2020
@author: Donald
"""
#imported modules to split or/and solve log expressions
from re import findall
import math

quit_options=[ 'x', 'q', 'exit', 'quit'] 

print("="*70)
print("Enter mathematical expression to perfom calculation.e.g 2 + 4 ... ")
print("Or Enter x, q, exit, or quit to end operation ...")
print("="*70)

while True:
    try:
        #functions to handle specific mathematical expressions
        def add(x,y):
            return x + y
    
        def subtract(x,y):
            return x - y
    
        def multiply(x,y):
            return x * y
    
        def divide(x,y):
            return x / y
    
        def natlog(exp):
            x = math.log(int(findall("\d+",exp)[0]))
            return x
    
        def base10log(exp):
            x = math.log10(int(findall("\d+",exp)[1]))
            return x
    
        def base2log(exp):
            x = math.log2(int(findall("\d+",exp)[1]))
            return x

        #prompt user for input
        exp = input(">> ").strip().replace(" ","").replace("ln","log")    
        if exp in quit_options:
            print("See you next time!!")
            break
        #split expressions 
        L = findall('[0-9.]+|\W|\w+\W\d+\W',exp)
        #to handle expressions with length of 1
        if len(L) == 1:        
            if "log10" in exp or "log2" in exp or "log" in exp:
                if "log10" in exp:
                    print(base10log(exp))
                elif "log2" in exp:
                    print(base2log(exp))
                elif "log" in exp:
                    print(natlog(exp))               
            elif exp.isdigit() or float(exp).is_integer:
                print(exp)        
        #to handle logs in expressions           
        calc=[]                            
        for e in L:
            if "log10" in e:
                calc.append(str(base10log(e))) 
            elif "log2" in e:
                calc.append(str(base2log(e)))            
            elif "log" in e:
                calc.append(str(natlog(e)))
            else:
                calc.append(e)
        #to handle expressions with length of 3 and one operator    
        if len(calc) == 3:
            num1, op, num2 = float(calc[0]),calc[1],float(calc[2])    
            if "+" in op:
                print(add(num1, num2))
            elif "-" in op:
                print(subtract(num1, num2))
            elif "*" in op:
                print(multiply(num1, num2))
            elif "/" in op:
                print(divide(num1, num2))        
        #to handle expressions with length of 5 and two operators
        elif len(calc) == 5:
            num1, op1, num2, op2, num3 = float(calc[0]), calc[1], float(calc[2]), calc[3], float(calc[4])
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
    #to catch errors occured        
    except Exception as e:
        print("Error: {}".format(e))
        print("Check input and try again")