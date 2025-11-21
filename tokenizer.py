import re

class Tokenizer:
    def validate_expression(self, expression): #Проверка по строкам
        if not expression.strip():
            raise ValueError("Пустое выражение")

        valid_chars = r'[\d\+\-\*\/\(\)\.\s]'
        invalid_chars = re.findall(f'[^{valid_chars[1:]}', expression)
        if invalid_chars:
            raise ValueError(f"Недопустимые символы: {set(invalid_chars)}")

        if re.search(r'\d+\.\d*\.', expression):
            raise ValueError("Некорректное число с множественными точками")

        if re.search(r'\d+\.(?!\d)', expression):
            raise ValueError("Некорректное число: точка без дробной части")

        bracket_stack = []
        for i, char in enumerate(expression):
            if char == '(':
                bracket_stack.append(i)
            elif char == ')':
                if not bracket_stack:
                    raise ValueError("Непарная закрывающая скобка")
                bracket_stack.pop()
        if bracket_stack:
            raise ValueError("Непарная открывающая скобка")

        cleaned = expression.replace(' ', '')
        if cleaned and cleaned[0] in ['*', '/']:
            raise ValueError("Выражение не может начинаться с оператора * или /")
        if cleaned and cleaned[-1] in ['+', '-', '*', '/']:
            raise ValueError("Выражение не может заканчиваться оператором")

        return True

    def validate_tokens(self, tokens): #Проверка по токенам
        if not tokens:
            raise ValueError("Нет токенов для вычисления")

        for i in range(len(tokens) - 1):
            current = tokens[i]
            next_token = tokens[i + 1]

            if current in ['+', '-', '*', '/']:
                if next_token in ['+', '-']:
                    raise ValueError(
                        f"После оператора '{current}' не может идти оператор '{next_token}', если оператор '{next_token}' унарный - пожалуйста, поставьте скобки")
                if next_token in ['*', '/']:
                    raise ValueError(f"После оператора '{current}' не может идти оператор '{next_token}'")

            if re.match(r'\d+\.?\d*', current) and next_token == '(':
                raise ValueError(f"После числа '{current}' не может идти открывающую скобку")

            if current == ')' and re.match(r'\d+\.?\d*', next_token):
                raise ValueError(f"После закрывающей скобки не может идти число '{next_token}'")

            if current == '(' and next_token in ['*', '/']:
                raise ValueError(f"После открывающей скобки не может идти оператор '{next_token}'")

        return True

    def tokenize(self, expression): #Разбиение на токены
        expression_no_spaces = expression.replace(' ', '')
        token_pattern = r'\d+\.?\d*|[\+\-\*\/\(\)]'
        tokens = re.findall(token_pattern, expression_no_spaces)

        remaining = re.sub(token_pattern, '', expression_no_spaces)
        if remaining:
            raise ValueError(f"Нераспознанные символы: '{remaining}'")

        self.validate_tokens(tokens)
        return tokens