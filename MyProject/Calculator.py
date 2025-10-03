from dataclasses import dataclass, field
from simpleeval import simple_eval
from safe_functions import SAFE_FUNCTIONS, SAFE_CONSTANTS


@dataclass
class Calculator:
    """Инженерный калькулятор с безопасными функциями и переменными."""

    functions: dict = field(default_factory=lambda: SAFE_FUNCTIONS.copy())
    constants: dict = field(default_factory=lambda: SAFE_CONSTANTS.copy())
    variables: dict = field(default_factory=dict)

    # ------------------ Основные методы ------------------
    def assign_variable(self, name: str, expr: str):
        """Присвоить значение переменной."""
        if name in self.functions or name in self.constants:
            raise ValueError(f"Нельзя переопределить зарезервированное имя: {name}")
        value = self._eval(expr)
        self.variables[name] = value
        return f"{name} = {value}"

    def evaluate_expression(self, expression: str):
        """Вычислить математическое выражение."""
        result = self._eval(expression)
        self.variables['ans'] = result
        return result

    def evaluate(self, expression: str):
        """Определить: присваивание или вычисление."""
        if "=" in expression:
            name, expr = map(str.strip, expression.split("=", 1))
            return self.assign_variable(name, expr)
        return self.evaluate_expression(expression)

    # ------------------ Внутренний метод ------------------
    def _eval(self, expression: str):
        """Обёртка для simple_eval."""
        return simple_eval(expression,
                           functions=self.functions,
                           names={**self.constants, **self.variables})
