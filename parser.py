import re


class Parser:
    def __init__(self):
        self.tokens = []
        self.pos = 0

    def get_current_token(self): #Возвращает текущий токен
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume_token(self): #Перемещает указатель на следующий токен
        self.pos += 1

    def parse(self, tokens):

        self.tokens = tokens
        self.pos = 0

        result = self.expr()

        if self.pos != len(self.tokens):
            next_token = self.get_current_token()
            raise ValueError(f"Некорректное выражение - необработанные токены, начиная с: '{next_token}'")

        return result

    def factor(self):

        token = self.get_current_token()

        if token is None:
            raise ValueError("Конец выражения")

        if token == '+' or token == '-':
            self.consume_token()
            value = self.factor()
            if token == '+':
                return value
            else:
                return -value

        if re.match(r'^\d+\.?\d*$', token):
            self.consume_token()
            return float(token)

        if token == '(':
            self.consume_token()
            result = self.expr()
            if self.get_current_token() != ')':
                raise ValueError("Ожидается закрывающая скобка")
            self.consume_token()
            return result

        raise ValueError(f"Неожиданный токен: '{token}'")

    def term(self): #Умножение и деление
        result = self.factor()

        while True:
            token = self.get_current_token()
            if token != '*' and token != '/':
                break

            self.consume_token()
            right = self.factor()

            if token == '*':
                result = result * right
            elif token == '/':
                if right == 0:
                    raise ValueError("Деление на ноль")
                result = result / right

        return result

    def expr(self): #Сложение и вычитание
        result = self.term()

        while True:
            token = self.get_current_token()
            if token != '+' and token != '-':
                break

            self.consume_token()
            right = self.term()

            if token == '+':
                result = result + right
            elif token == '-':
                result = result - right

        return result