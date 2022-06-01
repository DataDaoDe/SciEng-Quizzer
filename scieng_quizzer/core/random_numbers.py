import random

def get_random_natural(minimum: int = 1, maximum: int = 100):
    if minimum < 1 or maximum < 1:
        raise ValueError("no arguments can be less than 1.")

    return random.randint(minimum, maximum)

def get_random_integer(minimum: int = -100, maximum: int = 100):
    return random.randint(minimum, maximum)

def get_random_integer_nonzero(minimum: int = -100, maximum: int = 100):
    if maximum <= minimum:
        raise ValueError('maximum cannot be less than or equal to the minimum in the range.')
    
    num = random.randint(minimum, maximum)

    if num == 0:
        return get_random_integer_nonzero(minimum, maximum)
    else:
        return num