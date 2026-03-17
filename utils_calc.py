def add(num1, num2):
    result = num1+num2
    if isinstance(num1, float) or isinstance(num2, float):
        return float(result)
    
    return result

def sub(num1, num2):
    result = num1-num2
    if isinstance(num1, float) or isinstance(num2, float):
        return float(result)
    
    return result

def multiply(num1, num2):
    result = num1*num2
    if isinstance(num1, float) or isinstance(num2, float):
        return float(result)
    
    return result

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    
    result = num1 / num2
    
    if isinstance(num1, float) or isinstance(num2, float):
        return float(result)
    
    return result

def exponent(base, exp):
    result = num1**num2
    if isinstance(num1, float) or isinstance(num2, float):
        return float(result)
    
    return result

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