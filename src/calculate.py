from src.tokenize import tokenize
from src.shunting_yard import shunting_yard
from src.rpn_calc import rpn_calc


def calculate(expr: str) -> float:
    """
    Вычисляет выражение
    :param expr: Выражение
    :return: Возвращает результат выполнения выражения
    """
    tokenized = tokenize(expr)
    rpn = shunting_yard(tokenized)
    result = rpn_calc(rpn)

    return result
