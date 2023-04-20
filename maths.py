def calculate():
    """
    A simple calculator function that takes in user input and performs
    mathematical operations based on that input. It accepts numbers up to
    10 decimal places, and displays answers to the same precision.
    """
    while True:
        num1 = input("Enter a number (or 'q' to quit): ")
        if num1.lower() == 'q':
            break
        try:
            num1 = float(num1)
            op = input("Enter an operator (+, -, *, /): ")
            num2 = float(input("Enter another number: "))
            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                result = num1 / num2
            else:
                print("Invalid operator. Please try again.")
                continue
            print(f"Answer: {result:.10f}/n" if result % 1 else f"Answer: {int(result)}/n")
        except ValueError:
            print("Invalid input. Please try again.")
        else:
            if input("Press 'q' to quit or any other key to continue: ").lower() == 'q':
                break

if __name__ == '__main__':
    calculate()
