def factorial(num:int):
    '''  
    Calculate n! using recursion.
    
    Parameters
    ----------
    num : int
    
    Returns
    -------
    int
    '''
    if num <0:
        raise ValueError("Factorial is undefined negative values")
    if num == 0 or num == 1:
        return 1

    return num * factorial(num -1)


def is_prime(num:int)->bool:
    '''  
    Check whether a number is prime.
    
    Parameters
    ----------
    num : int
    Number to test.
    
    Returns
    -------
    bool
    True if prime, otherwise False.
    
    '''

    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def common_divisors(num1: int, num2: int) -> list[int]:
    limit = min(num1, num2)
    divisors = []

    for divisor in range(1, limit+1):
        if num % divisor == 0 and num2 % divisor ==0:
            divisors.append(divisor)
    return divisor