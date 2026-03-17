def add(num1, num2):
    if num1 is int & num2 is int:
        sum = int(num1+num2)
    else:
        sum = num1+num2
    return sum

def sub(num1, num2):
    if num1 is int & num2 is int:
        dif = int(num1-num2)
    else:
        dif = num1-num2
    return dif

def multiply(num1, num2):
    if num1 is int & num2 is int:
        mult = int(num1*num2)
    else:
        mult = num1*num2
    return mult

def divide(num1, num2):
    if num2 == 0:
        div = "Error: Division by zero is not allowed."
        print(div)
    else:
        div = num1/num2
    return div

def exponent(base, exp):
    if base is int & exp is int:
        power = int(base**exp)
    else:
       power = base**exp
       
    return power

def modulo(num1, num2):
    if num2 == 0:
        mod = "Error: Division by zero is not allowed."
        print(mod)
    elif num1 is int & num2 is int:
        mod = int(num1 % num2)
    else:
        mod = num1 % num2
    return mod

def floor_divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    
    result = num1 // num2
    
    if isinstance(num1, float) or isinstance(num2, float):
        return float(result)
    
    return result

def absolute(num):
    if num is int:
        if num >=0:
            abs = num
        else:
            abs = -1*num
            
    else:
        if num >=0:
            abs = num
        else:
            abs = -1*num
    return abs