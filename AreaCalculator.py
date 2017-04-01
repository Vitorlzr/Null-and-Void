def triangle(num1, num2):
    return 1/2 * num1 * num2

def square(num1):
    return num1**2

def rectangle(num1, num2):
    return num1 * num2

def para(num1, num2):
    return num1 * num2
	
def main():
    operation = input("Choose the shape (square, triangle, rectangle, parallelogram) ") 
	
    if(operation != 'square' and operation != 'triangle' and operation  != 'rectangle' and operation != 'parallelogram'):
        print("You must enter a valid operation" (main()))
	
    elif(operation == 'square'):
        var0 = int(input("Enter the side: "))
	
	
    else: 
        var1 = int(input("Enter side1: "))
        var2 = int(input("Enter side2: "))

		
    
    if(operation == 'triangle'):
        print(triangle(var1, var2))
    
    elif(operation == 'square'):
        print(square(var0))
    
    elif(operation == 'parallelogram'):
        print(para(var1, var2))
    
    else:
        print(rectangle(var1, var2))
    while True:
	    print(main())
main() 
    
        



		  
	

