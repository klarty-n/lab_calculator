import re
from src.calc_exceptions import ExpressionError

token_re = re.compile(r"\s*([+-]?\d+(?:\.\d+)?|\*\*|//|[+\-*/%()])")
Token = tuple[str, float|None]


def tokenize(expr: str) -> list[Token]:
    """
    Разбиение выражения на токены
    :param expr: выражение
    :return: список токенов
    """
    if not expr or not expr.strip():
        raise ExpressionError("Пустой ввод")
    expr = expr.replace(',','.')

    tokenized: list[Token] = []
    pos = 0

    while pos < len(expr):
        #Ищем первое совпадение шаблону
        matches = token_re.match(expr,pos)
        if not matches:
            raise ExpressionError ('Неизвестный символ')

        tok = matches.group(1)
        #Сдвигаемся в конец токена
        pos = matches.end()

        if tok[0].isdigit():
            tokenized.append(('NUM', float(tok)))
        elif len(tok)>1 and tok[1].isdigit():
            if tok[0] == '+':
                tokenized.append(( '$',None))
                tokenized.append(('NUM', float(tok[1:])))
            else:
                tokenized.append(( '~', None))
                tokenized.append(('NUM', float(tok[1:])))
        else:
            tokenized.append((tok,None))


    tokenized.append(('End',None))
    return tokenized
