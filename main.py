from tokenizer import Tokenizer
from parser import Parser
from tests import run_comprehensive_tests  # ← перенести импорт сюда

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

def main():
    calculator = Calculator()

    print("Консольный калькулятор, задание E1")
    print("Поддерживаемые операции: +, -, *, /, унарные +/-, скобки")
    print("Команды:")
    print("  'quit' - выход")
    print("  'test' - запуск тестов")
    print("-" * 60)

    while True:
        try:
            user_input = input("Введите выражение или команду: ").strip()

            if user_input.lower() == 'quit':
                break
            elif user_input.lower() == 'test':
                run_comprehensive_tests()
                continue
            elif not user_input:
                continue

            result = calculator.calculate(user_input)
            print(f"Результат: {result}")

        except ValueError as e:
            print(f"Ошибка: {e}")
        except KeyboardInterrupt:
            print("\nВыход из программы")
            break
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")

if __name__ == "__main__":
    main()