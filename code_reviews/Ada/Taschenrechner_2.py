def amount_of_calculations(amount_input):
    return int(amount_input)

def parse_input(text_input):
    operators = "+-*/~"
    gefunden = False
    operator_index=0
    operator = ""

    for index in range(len(text_input)):
        if text_input[index]in operators and gefunden == False:
            operator_index = index
            operator = text_input[index]
            gefunden = True

    num1_text = text_input[:operator_index]
    num2_text= text_input[operator_index+1:]

    num1 = float(num1_text)
    num2 = float(num2_text)

    return num1, operator, num2

def calculate (num1, operator, num2):
    if operator == "+":
        return num1 +num2
    elif operator == "-":
        return num1-num2
    elif operator == "/":
        return num1/num2
    elif operator =="*":
        return num1*num2
    elif operator == "~":
        return num1//num2, num1%num2


def display_results (result,operator):
    if operator == "~":
        print(f"The answer is {result[0]}")
        print(f"The remainder is {result[1]}")
    else:
        print(f"The answer is {result}")

def run_calculations(amount):
    for i in range (amount):
        user_input=input("What do you want to calculate?")
        num1, operator, num2 = parse_input(user_input)
        result = calculate(num1, operator, num2)
        display_results(result,operator)

def main():
    print("Welcome to the Python calculator")

    amount_user_input = input("How many calculations do you want to implement? ")
    amount = amount_of_calculations(amount_user_input)
    run_calculations(amount)


if __name__ =="__main__":
    main()

