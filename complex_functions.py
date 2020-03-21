"""
Useful functions.
"""

import math
import numpy as np


def complex_sum(a1, b1, a2, b2):
    return complex(a1 + a2, b1 + b2)


def complex_subtraction(a1, b1, a2, b2):
    return complex(a2 - a1, b2 - b1)


def complex_mult(a1, b1, a2, b2):
    return complex(a1*a2 - b1*b2, a1*b2 + a2*b1)


def complex_division(a1, b1, a2, b2):
    return complex(
        (a1*a2 + b1*b2)/((a2**2) + (b2**2)),
        (a2*b1 - a1*b2)/((a2**2) + (b2**2))
        )


def complex_conjugate(a1, b1):
    return complex(a1, -b1)


def complex_module(a1, b1):
    return (a1**2 + b1**2)**(1/2)


def polar_cartesian(p, theta):
    return complex(p*math.cos(theta), p*math.sin(theta))


def cartesian_polar(a1, b1):
    p = (a1**2 + b1**2)**(1/2)
    theta = math.atan(b1/a1)
    return [p, theta]


def matrix_inverse(m1):
    return np.linalg.inv(m1)


def matrix_scalar_multiplication(m1, a):
    return a*m1


def matrix_multiplication(m1, m2):
    return np.matmul(m1, m2)


def dot_product(vector1, vector2):
    cont = 0
    for i in range(0, 2):
        cont = cont + vector1[i]*vector2[i]
        return cont


def vector_norm(vector):
    cont = 0
    for i in range(0, 2):
        cont = cont + (vector[i]**2)
