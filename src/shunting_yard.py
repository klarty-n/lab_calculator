from src.calc_exceptions import ExpressionError
from src.tokenize import Token
from src.token import operators

Tokens = tuple[str|float]

def shunting_yard(tokenized: list[Token]) -> list[Tokens]:
    """
    Шунтирующий двор со скобками
    :param tokenized: Список токенов в инфиксной нотации
    :return: Возвращает список токенов в RPN
    """
    result: list[float|str] = []
    stack: list[str] = []

    for token, value in tokenized:
        if token == 'End':
            break

        if token == 'NUM':
            result.append(value)    # type: ignore

        elif token in'$~':
            stack.append(token)

        #
        elif token in operators:
            op1 = token #текущий токен
            op1_info = operators[op1]

            while stack and stack[-1] in operators:
                op2 = stack[-1] #токен с верхушки стека
                op2_info = operators[op2]

                #Сравниваем приоритеты и ассоциативность для текущего токена и верхушки стека
                if ((op1_info.associativity =='left' and op1_info.prio <= op2_info.prio) or
                    (op1_info.associativity == 'right' and op1_info.prio < op2_info.prio)):
                    result.append(stack.pop())
                else:
                    break

            stack.append(op1)

        elif token == '(':
            stack.append(token)

        elif token == ')':
            # "Выталкиваем" из стека все, что стоит до открывающкй скобки
            while stack and stack[-1] != '(':
                result.append(stack.pop())

            if stack:
                # Убираем из стека открывающую скобку
                stack.pop()
            else:
                raise ExpressionError('Несогласованные скобки')

    #"Выталкиваем" оставшиеся в стеке операции
    while stack:
        op = stack.pop()

        if op[-1] == '(':
            raise ExpressionError('Несогласованные скобки')
        result.append(op)

    return result       # type: ignore
