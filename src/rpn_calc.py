from src.calc_exceptions import ExpressionError, CalcError
from src.shunting_yard import Tokens


def is_int(x: float) -> bool:
    """
    Проверка, является ли число целым
    :param x: число для проверки
    :return: True если число целое
    """
    return x == int(x)


def rpn_calc(rpn_tokens: list[Tokens]) -> float:
    """
    Вычисление выражения в обратной польской записи при помощи стека
    :param rpn_tokens: список токенов в RPN
    :return: результат вычисления, последнее оставшееся в стеке число
    """
    stack: list[float] = []

    for token in rpn_tokens:
        #Если токен - число, кладем сразу в стек
        if token not in ('~', '$', '**', '*', '/', '//', '%', '+', '-'):
            stack.append(token)     # type: ignore
        elif token in ('~', '$', '**', '*', '/', '//', '%', '+', '-'):
            if token in '$~':       # type: ignore
                if not stack:
                    raise ExpressionError("Недостаточно операндов")
                a = stack.pop()
                if token == '$':
                    stack.append(+a)
                else:  # '~'
                    stack.append(-a)
            #Бинарные операторы
            else:
                if len(stack) < 2:
                    raise ExpressionError("Недостаточно операндов")
                right = stack.pop() #Правый операнд
                left = stack.pop() #Левый операнд

                try:
                    if token == '**':
                        result = left ** right
                    elif token == '*':
                        result = left * right
                    elif token == '/':
                        if right == 0:
                            raise CalcError("Деление на ноль")
                        result = left / right
                    elif token == '//':
                        if right == 0:
                            raise CalcError("Деление на ноль")
                        if not (is_int(left) and is_int(right)):
                            raise CalcError("Операции // и % только для целых чисел доступны")
                        result = left // right
                    elif token == '%':
                        if left == 0:
                            raise CalcError("Деление на ноль")
                        if not (is_int(left) and is_int(right)):
                            raise CalcError("Операции // и % только для целых чисел доступны")
                        result = left % right
                    elif token == '+':
                        result = left + right
                    elif token == '-':
                        result = left - right
                    else:
                        raise CalcError(f"Неизвестный оператор: {token}")

                    stack.append(result)

                except CalcError:
                    raise CalcError("Ошибка вычисления")

        else:
            raise ExpressionError(f"Неизвестный токен в RPN: {token}")

    if len(stack) != 1:
        raise ExpressionError("Некорректное выражение")

    return stack[0]
