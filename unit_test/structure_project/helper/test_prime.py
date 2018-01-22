def is_prime(number):
    '''
    Return True if the number is prime
    '''
    for element in range(2,number):
        if number % element == 0:
            return False
    return True
