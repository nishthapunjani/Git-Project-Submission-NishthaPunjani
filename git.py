def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error: Division by Zero"
def power(x, y): return x ** y

def calculator():
    print("Select: 1.Add 2.Sub 3.Mul 4.Div 5.Pow 6.Quit")
    while True:
        choice = input("\nChoice: ")
        
        # Check for option 6 or the word "quit"
        if choice == '6' or choice.lower() == 'quit': 
            print("Goodbye!") # Added your custom message here
            break
            
        if choice in ('1', '2', '3', '4', '5'):
            try:
                n1 = float(input("Num 1: "))
                n2 = float(input("Num 2: "))
                ops = {'1': add, '2': subtract, '3': multiply, '4': divide, '5': power}
                print("Result:", ops[choice](n1, n2))
            except ValueError: 
                print("Invalid number.")
        else: 
            print("Invalid choice.")

if __name__ == "__main__":
    calculator()
