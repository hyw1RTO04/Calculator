from Calculator import Calculator


def main():
    print("=== Калькулятор для вычислений ===")

    calc = Calculator()

    while True:
        try:
            expr = input(">>> ").strip()
            if expr.lower() in {"quit", "exit", "выход"}:
                print("Выход из калькулятора...")
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

if __name__ == "__main__":
    calc = Calculator()
    main()
