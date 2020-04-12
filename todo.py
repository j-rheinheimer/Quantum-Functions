# TODO


def matrix_inverse(m1):
    """
    """
    np.linalg.inv(m1)
    return


def matrix_scalar_multiplication(m1, a):
    """
    """
    a*m1
    return


def matrix_multiplication(m1, m2):
    """
    """
    np.matmul(m1, m2)
    return


def vector_norm(vector):
    """
    """
    cont = 0
    for i in range(0, 2):
        cont = cont + (vector[i]**2)
