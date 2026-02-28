def add(x: float, y: float) -> float:
    """Adds two numbers."""
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x + y

def subtract(x: float, y: float) -> float:
    """Subtracts the second number from the first."""
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x - y

def multiply(x: float, y: float) -> float:
    """Multiplies two numbers."""
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x * y

def divide(x: float, y: float) -> float:
    """Divides the first number by the second. Raises ValueError on division by zero."""
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def power(x: float, y: float) -> float:
    """Calculates x raised to the power of y."""
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x ** y

def add_three(x: float, y: float, z: float) -> float:
    """Adds three numbers."""
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float)) and isinstance(z, (int, float))):
        raise ValueError("All inputs must be numbers.")
    return x + y + z
