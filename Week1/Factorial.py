

def _factorial():
    number = int(input("Enter value to get factorial: "))
    global fact 
    fact = 1
    if number < 0:
        print("Invalid value to generate factorial")
        return 0

    if number == 0 or number == 1:
        return number
    else:
        while number > 1:
            fact = fact * number
            number -= 1
        return fact


if __name__ == "__main__":
    result = _factorial()
    if result != 0:
        print("factorial = ", result)
