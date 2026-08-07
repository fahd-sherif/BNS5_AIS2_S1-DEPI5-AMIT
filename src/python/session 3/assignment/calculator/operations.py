def add(num1, num2):
    """
    Add two numbers.
    :param num1: The first number.
    :type num1: float
    :param num2: The second number.
    :type num2: float
    :return: The sum of the two numbers.
    :rtype: float
    """
    return num1 + num2

def subtract(num1, num2):
    """
    Subtract the second number from the first.
    :param num1: The first number.
    :type num1: float
    :param num2: The second number.
    :type num2: float
    :return: The difference between the two numbers.
    :rtype: float
    """
    return num1 - num2


def multiply(num1, num2):
    """
    Multiply two numbers.
    :param num1: The first number.
    :type num1: float
    :param num2: The second number.
    :type num2: float
    :return: The product of the two numbers.
    :rtype: float
    """
    return num1 * num2


def divide(num1, num2):
    """
    Divide the first number by the second.
    :param num1: The dividend.
    :type num1: float
    :param num2: The divisor.
    :type num2: float
    :raise ZeroDivisionError: If the divisor is zero.
    :return: The division result.
    :rtype: float
    """
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return num1 / num2