from typing import List, Any
from sympy import Naturals, Symbol

# form: (a_n)x^n + (a_n-1)x^(n-1) + ... + (a_1)x + a_0

def create_polynomial(variable: Symbol, degree: int = 0, coeff_mat: List[Any] = []):
    idx = 0
    indeterminates = []
    if len(coeff_mat) != degree + 1:
        raise ValueError("The size of coefficient matrix must equal the degree of the polynomial plus 1.")
    
    while idx <= degree:
        v = variable ** idx
        indeterminates.append(v)
        idx += 1

    expression = None

    for item in zip(coeff_mat, indeterminates):
        term = item[0]*item[1] # (a_j)x^j
        if not expression:
            expression = term
        else:
            expression += term

    return expression