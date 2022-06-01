from sympy import Symbol, diff, latex
from scieng_quizzer.core.function_creator import create_polynomial
from scieng_quizzer.core.random_numbers import get_random_natural

DEFAULT_VAR_X = Symbol("x")
DEFAULT_VAR_Y = Symbol("y")

class FunctionOf2Var_UnknownPolynomial:

    def __init__(
        self, 
        var1: str = DEFAULT_VAR_X,
        var2: str = DEFAULT_VAR_Y,
        degrees = [1,1]
    ):
        self._var1 = var1
        self._var2 = var2
        self._degrees = degrees
        self._deriv_var1 = None
        self._deriv_var2 = None
        self._unknown_function = None
        self.create()

    def create(self):
        c1_mat = self._build_coeff_mat(self._degrees[0])
        c2_mat = self._build_coeff_mat(self._degrees[1])
        p1 = create_polynomial(self._var1, degree=self._degrees[0], coeff_mat=c1_mat)
        p2 = create_polynomial(self._var2, degree=self._degrees[1], coeff_mat=c2_mat)
        uf = p1 + p2
        dv1 = diff(uf, self._var1)
        dv2 = diff(uf, self._var2)
        self._unknown_function = uf
        self._deriv_var1 = dv1
        self._deriv_var2 = dv2


    def _build_coeff_mat(self, degrees: int):
        coeffs = []
        idx = 0
        
        while idx <= degrees:
            num = get_random_natural(maximum=10)
            coeffs.append(num)
            idx += 1

        return coeffs

    def unknown_function(self):
        return self._unknown_function

    def deriv_vars(self):
        return [self._deriv_var1, self._deriv_var2]


    def question_in_latex(self):
        lhs = f"({latex(self._deriv_var1)})d{self._var1}"
        rhs = f"({latex(self._deriv_var2)})d{self._var2}"
        return f"{lhs} + {rhs} = 0"