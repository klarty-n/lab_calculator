from src.calculate import calculate
from src.calc_exceptions import CalcError
from src.calc_exceptions import ExpressionError

def main() -> None:
    """
    Точка входа программы
    """
    while expr := input("Введите выражение: "):
        if expr == "exit_calc":
            exit()

        try:
            result = calculate(expr)
            print(result)

        except ExpressionError:
            print("Ошибка ввода")
        except CalcError:
            print("Ошибка выполнения")


if __name__ == "__main__":
    main()
