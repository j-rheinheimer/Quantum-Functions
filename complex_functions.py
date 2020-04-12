"""
Funções complexas
"""

import math


def complex_sum(a1: float, b1: float, a2: float, b2: float) -> complex:
    """
    Função que realiza a soma de dois números complexos

    Parâmetros:
    a1 (float): Parte real do primeiro número complexo
    b1 (float): Parte imaginária do primeiro número complexo
    a2 (float): Parte real do segundo número complexo
    b2 (float): Parte imaginária do segundo número complexo

    Retorno:
    soma (complex): Soma dos números complexos anteriores
    """
    soma = complex(a1 + a2, b1 + b2)
    return soma


def complex_subtraction(a1: float, b1: float, a2: float, b2: float) -> complex:
    """
    Função que realiza a subtração de dois números complexos

    Parâmetros:
    a1 (float): Parte real do primeiro número complexo
    b1 (float): Parte imaginária do primeiro número complexo
    a2 (float): Parte real do segundo número complexo
    b2 (float): Parte imaginária do segundo número complexo

    Retorno:
    sub (complex): Subtração dos números complexos anteriores
    """
    sub = complex(a2 - a1, b2 - b1)
    return sub


def complex_mult(a1: float, b1: float, a2: float, b2: float) -> complex:
    """
    Função que realiza a multiplicação de dois números complexos

    Parâmetros:
    a1 (float): Parte real do primeiro número complexo
    b1 (float): Parte imaginária do primeiro número complexo
    a2 (float): Parte real do segundo número complexo
    b2 (float): Parte imaginária do segundo número complexo

    Retorno:
    mult (complex): Multiplicação dos números complexos anteriores
    """
    mult = complex(a1*a2 - b1*b2, a1*b2 + a2*b1)
    return mult


def complex_division(a1: float, b1: float, a2: float, b2: float) -> complex:
    """
    Função que realiza a divisão de dois números complexos

    Pârametros:
    a1 (float): Parte real do primeiro número complexo
    b1 (float): Parte imaginária do primeiro número complexo
    a2 (float): Parte real do segundo número complexo
    b2 (float): Parte imaginária do segundo número complexo

    Retornos:
    div (complex): Divisão dos números complexos anteriores
    """
    div = complex(
        (a1*a2 + b1*b2)/((a2**2) + (b2**2)),
        (a2*b1 - a1*b2)/((a2**2) + (b2**2))
        )
    return div


def complex_conjugate(a1: float, b1: float) -> complex:
    """
    Função que obtem o conjugado de um número complexo

    Parâmetros:
    a1 (float): Parte real do número complexo
    b1 (float): Parte imaginária do número complexo

    Retorno:
    conj (complex): Conjugado do número complexo fornecido
    """
    conj = complex(a1, -b1)
    return conj


def complex_module(a1: float, b1: float) -> float:
    """
    Função que obtem o módulo de um número complexo

    Parâmetros:
    a1 (float): Parte real do número complexo
    b1 (float): Parte imaginária do número complexo

    Retorno:
    mod (float): Módulo do número complexo fornecido
    """
    mod = (a1**2 + b1**2)**(1/2)
    return mod


def polar_cartesian(p: float, theta: float) -> list:
    """
    Função que converte um número complexo de sua forma polar
    para sua forma cartesiana

    Parâmetros:
    p (float): Módulo do número complexo
    theta (float): Fase do número complexo

    Retorno:
    cart (list[a (float), b (float)]): lista contendo o valor (a) real e o
    valor imaginário (b) do número complexo convertido
    """
    a = p*math.cos(theta)
    b = p*math.sin(theta)
    cart = [a, b]
    return cart


def cartesian_polar(a1: float, b1: float) -> list:
    """
    Função que converte um número complexo de sua forma cartesiana
    para sua forma polar

    Parâmetros:
    a1 (float): Parte real do número complexo
    b1 (float): Parte imaginária do número complexo

    Retorno:
    pol (list[p (float), theta (float)]): lista contendo o valor do
    módulo (p) e da fase (theta) do número complexo convertido
    """
    p = (a1**2 + b1**2)**(1/2)
    theta = math.atan(b1/a1)
    pol = [p, theta]
    return pol


def dot_product(vector1: list, vector2: list) -> float:
    """
    Função para calcular o produto escalar entre dois vetores

    Parâmetros:
    vector1 (list):
    vector2 (list):

    Retorno:
    cont (float):
    """
    cont = 0
    for i in range(0, 2):
        cont = cont + vector1[i]*vector2[i]
    return cont
