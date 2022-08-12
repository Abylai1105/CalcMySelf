import func as type
import input_data

def button_click():
    a = input_data.get_value()
    b = input_data.get_value()
    op = input("Введите оператцию: +, -, *, / \n")
    if op == "+":
        result = type.plus(a, b)
    elif op == "-":
        result = type.minus(a, b)
    elif op == "*":
        result = type.multiply(a, b)
    elif op == "/":
        result = type.devide(a, b)
    input_data.data(result)
    return result