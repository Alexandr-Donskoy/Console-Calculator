from tokenizer import Tokenizer
from parser import Parser


class Calculator:
    def __init__(self):
        self.tokenizer = Tokenizer()
        self.parser = Parser()

    def calculate(self, expression):
        try:
            # Валидация и токенизация
            self.tokenizer.validate_expression(expression)
            tokens = self.tokenizer.tokenize(expression)

            # Вычисление
            result = self.parser.parse(tokens)

            return result

        except Exception as e:
            raise ValueError(f"Ошибка вычисления: {str(e)}")