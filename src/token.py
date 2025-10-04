class OperatorInfo:
    def __init__(self, prio: int, associativity: str = 'left'):
        self.prio = prio
        self.associativity = associativity

# Информация об операторах (приоритет, ассоциативност)
operators = {
    '$': OperatorInfo(4),  # унарный плюс
    '~': OperatorInfo(4),  # унарный минус
    '**': OperatorInfo(3, 'right'),
    '*': OperatorInfo(2),
    '/': OperatorInfo(2),
    '//': OperatorInfo(2),
    '%': OperatorInfo(2),
    '+': OperatorInfo(1),
    '-': OperatorInfo(1)
}
