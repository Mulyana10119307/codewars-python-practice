def basic_op(operator, value1, value2):
    #your code here
    match operator:
        case "+":
            return value1 + value2
        case "-":
            return value1 - value2
        case "*":
            return value1 * value2
        case "/":
            return value1 / value2
        
print(basic_op("+", 2,5))
print(basic_op("*", 2,5))
print(basic_op("-", 2,5))
print(basic_op("/", 2,5))


