import math


def safe_factorial(n: int) -> int:
    """Безопасный факториал (ограничение до 10000)."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("factorial: n должно быть неотрицательным целым числом")
    if n > 10000:
        raise ValueError("factorial: n слишком большое (макс 10000)")
    return math.factorial(n)


# ------------------ Словари функций и констант ------------------
SAFE_FUNCTIONS = {
    'sqrt': math.sqrt, 'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
    'asin': math.asin, 'acos': math.acos, 'atan': math.atan,
    'log': math.log, 'log10': math.log10, 'exp': math.exp,
    'abs': abs, 'round': round, 'pow': pow, 'factorial': safe_factorial,
    'degrees': math.degrees, 'radians': math.radians,
}

SAFE_CONSTANTS = {
    'pi': math.pi, 'e': math.e, 'tau': math.tau
}
