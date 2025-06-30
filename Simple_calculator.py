k = 1
while(k>0):
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Modulo")
    print("6 - Exit")
    
    try:
        ch = int(input("Enter the option: "))

        if ch in [1, 2, 3, 4, 5, 6]:
            
            
        
            if ch == 1:
                a = float(input("Enter the value of a: "))
                b = float(input("Enter the value of b: "))
                c = a + b
                print(f"Sum = {c}\n")
            
            elif ch == 2:
                a = float(input("Enter the value of a: "))
                b = float(input("Enter the value of b: "))
                if(a>=b):
                    c = a - b
                    print(f"Subtraction = {c}\n")
                else:
                    print("1st number is smaller than 2nd number\n")
            elif ch == 3:
                a = float(input("Enter the value of a: "))
                b = float(input("Enter the value of b: "))
                c = a * b
                print(f"Multiplication = {c}\n")
            
            elif ch == 4:
                a = float(input("Enter the value of a: "))
                b = float(input("Enter the value of b: "))
                if b != 0:
                    c = a / b
                    print(f"Division = {c:.2f}\n")
                else:
                    print("Division by zero is not allowed.\n")
            
            elif ch == 5:
                a = float(input("Enter the value of a: "))
                b = float(input("Enter the value of b: "))
                c = a % b
                print(f"Modulo = {c}\n")
            elif(ch == 6) :
                print("Exiting the program....")
                break
                
                
        
        else:
            print("Invalid main option.\n")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.\n")

k = k+1

print("rerun the program")