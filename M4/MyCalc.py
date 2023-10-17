""" Basic Calc class used to demonstrate test cases via test_calc.py"""
""" 
UCID: krs
Date: 10/11/23
"""
class Calc:
    def __init__(self) -> None:
        self.ans = None

    def add(self, a,b):         # Addition function
        self.ans = a+b

    def sub(self, a,b):         # Subtraction function
        self.ans = a-b
    
    def mult(self, a,b):        # Multiplication Function
        self.ans = a*b
    
    def div(self, a,b):         # Division Function
        if b == 0:
            self.ans = "Cannot divide by zero"
        else:
            self.ans = a/b

# UCID: krs     # Date: 10/11/23

    def run(self):
        while True:
            # Take user input in the given format
            user_input = input("Enter a math expression (2 * 2 or ans + 5): ")

            # quit helps tp break the while loop
            if user_input.lower() == "quit":
                break
            
            # ans helps to print the last answer calculated
            if user_input.lower() == "ans":
                if self.ans is None:
                    print("No calculations made yet.")
                else:
                    print("ans:", self.ans)
                continue

            # input expression with previous answer and new operator with new num2 value
            if user_input.startswith("ans "):

                # Extract the operator and num2 value
                parts = user_input.split()

                # Checks that 3 parts exists and second part is an operator
                if len(parts) == 3 and parts[1] in ["+", "-", "*", "/"]:
                    operator = parts[1]

                    # Converting the num2 value as float and storing in value
                    value = float(parts[2])
                    if operator == "+":
                        self.add(self.ans, value)
                    elif operator == "-":
                        self.sub(self.ans, value)
                    elif operator == "*":
                        self.mult(self.ans, value)
                    elif operator == "/":
                        if value == 0:          # Taking care of divide by zero exception
                            print("Cannot divide by zero")
                        else:
                            self.div(self.ans, value)
                    print("ans:", self.ans)
                else:
                    print("Invalid input. Use 'ans + 5' format.")
                continue
            
            # Splitting the expression into 3 parts
            parts = user_input.split()

            if len(parts) != 3:
                print("Invalid input. Please enter a valid expression.")
                continue

            # Storing the 3 parts as num1, operator, num2 respectively
            num1, operator, num2 = parts

            try:
                num1 = float(num1)
                num2 = float(num2)
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                continue

            # Perform the calculation based on the operator
            if operator == "+":
                self.add(num1, num2)
            elif operator == "-":
                self.sub(num1, num2)
            elif operator == "*":
                self.mult(num1, num2)
            elif operator == "/":
                self.div(num1, num2)

            else:
                print("Invalid operator. Please use +, -, *, or /.")

            print("Result: ", self.ans)

if __name__ == "__main__":
    calc = Calc()
    calc.run()
