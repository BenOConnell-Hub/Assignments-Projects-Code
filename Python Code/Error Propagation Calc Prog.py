import sympy as sp
import numpy as np

def propagate_error(formula, variables, values, errors):
    """
    General error propagation for any formula.

    Parameters
    ----------
    formula : sympy expression
        The formula f(x1, x2, ..., xn)
    variables : list of sympy symbols
        [x1, x2, ..., xn]
    values : list or array
        Numerical values of variables
    errors : list or array
        Corresponding uncertainties

    Returns
    -------
    value : float
        Numerical value of the formula
    error : float
        Propagated uncertainty
    """

    # Evaluate the function
    substitutions = dict(zip(variables, values))
    value = float(formula.evalf(subs=substitutions))

    # Compute propagated error
    error_squared = 0.0
    for var, err in zip(variables, errors):
        partial = sp.diff(formula, var)
        partial_value = float(partial.evalf(subs=substitutions))
        error_squared += (partial_value * err) ** 2

    error = np.sqrt(error_squared)
    return value, error

A, D = sp.symbols('A D')

n_formula = sp.sin((A + D)/2) / sp.sin(A/2)

# Values in radians!
A_val = np.deg2rad(59.57)
D_val = np.deg2rad(39.46)

A_err = np.deg2rad(0.03)
D_err = np.deg2rad(0.03)

value, error = propagate_error(
    n_formula,
    [A, D],
    [A_val, D_val],
    [A_err, D_err]
)

print(f"n = {value:.6f} ± {error:.6f}")

