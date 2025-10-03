from Calculator import Calculator


def main():
    print("=== Калькулятор для вычислений ===")

    calc = Calculator()

    while True:
        try:
            expr = input(">>> ").strip()
            if expr.lower() == "quit":
                print("Выход...")
                break

            print(calc.evaluate(expr))

        except ValueError as e:
            print(f"Ошибка значения: {e}")
        except SyntaxError as e:
            print(f"Синтаксическая ошибка: {e}")
        except KeyboardInterrupt:
            print("\nПрервано пользователем. Выход...")
            break
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")


# ------------------ Мини-тесты ------------------
if __name__ == "__main__":
    calc = Calculator()

    # Проверка простых выражений
    assert calc.evaluate("2+2") == 4
    assert round(calc.evaluate("sqrt(16)")) == 4
    assert calc.evaluate("factorial(5)") == 120

    # Проверка присваивания
    assert calc.evaluate("x = 10") == "x = 10"
    assert calc.evaluate("x + 5") == 15

    # Проверка констант
    assert round(calc.evaluate("pi"), 2) == 3.14

    print("✅ Все встроенные тесты прошли успешно!")

    main()
