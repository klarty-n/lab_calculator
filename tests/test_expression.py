from src.calculate import calculate
from src.calc_exceptions import ExpressionError, CalcError
import pytest

class TestExpressions:
    def test_basic_arithmetic(self):
        """
        Тест простых выражений
        """
        assert calculate("666 + 3") == 669
        assert calculate("666 - 3") == 663
        assert calculate("666 * 3") == 1998
        assert calculate("666 / 2") == 333
        assert calculate("666 / 4") == 166.5

    def test_exponentiation(self):
        """
        Тестирование возведения в степень
        """
        assert calculate("2 ** 3") == 8
        assert calculate("4 ** 0.5") == 2
        assert calculate("3 ** 2 ** 2") == 81  # правоассоциативность проверяем

    def test_unary_operators(self):
        """
        Тест унарных операторов
        """
        assert calculate("+5") == 5
        assert calculate("-5") == -5
        assert calculate("5 + -3") == 2
        assert calculate("5 - +3") == 2

    def test_parentheses(self):
        """
        Тест приоритета операций и скобок
        """
        assert calculate("(2 + 3) * 4") == 20
        assert calculate("2 + 3 * 4") == 14
        assert calculate("(2 + 3) * (4 - 1)") == 15
        assert calculate("2 * (3 + 4)") == 14

    def test_complex_expressions(self):
        """
        Тест сложных выражений
        """
        assert calculate("2 + 3 * 4 - 5 / 2") == 11.5
        assert calculate("(2 + 3) * (4 - 1) ** 2") == 45
        assert calculate("10 + 2 * 3 - 4 / 2") == 14
        assert calculate("2 ** 3 * 4 + 1") == 33

    def test_floats(self):
        """
        Тест операций с дробными числами
        """
        assert calculate("2.5 + 3.5") == 6.0
        assert calculate("3.5 * 2") == 7.0
        assert calculate("5.5 / 2") == 2.75

class TestError:

    def test_number_tokenization(self):
        """
        Тестирует неправильную запись числа
        """
        with pytest.raises(ExpressionError):
            calculate(".")
        with pytest.raises(ExpressionError):
            calculate("1.0.0")


    def test_syntax(self):
        """
        Тестирует синтаксис выражения
        """
        with pytest.raises(ExpressionError):
            calculate("")
        with pytest.raises(ExpressionError):
            calculate(" ")
        with pytest.raises(ExpressionError):
            calculate("--+-")

        with pytest.raises(ExpressionError):
            calculate("(* ^ ‿ ^ *)")
        with pytest.raises(ExpressionError):
            calculate("(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
        with pytest.raises(ExpressionError):
            calculate("	(＠＾◡＾)")

        with pytest.raises(ExpressionError):
            calculate(":)")
        with pytest.raises(ExpressionError):
            calculate("(((")
        with pytest.raises(ExpressionError):
            calculate(")")

        with pytest.raises(ExpressionError):
            calculate("(66+6")
        with pytest.raises(ExpressionError):
            calculate("(5640))(23))))=+))(")
        with pytest.raises(ExpressionError):
            calculate("(0)  665    (0)")



    def test_calculation(self):
        """
        Тестирует деление(в том числе на 0)
        """
        with pytest.raises(CalcError):
            calculate("1/0")
        with pytest.raises(CalcError):
            calculate("1//0")

        with pytest.raises(CalcError):
            calculate("455.3//2")
        with pytest.raises(CalcError):
            calculate("3.4//6.66")

        with pytest.raises(CalcError):
            calculate("455.3%440")
        with pytest.raises(CalcError):
            calculate("12%4555.9")
