from calculator import Calculator

def run_comprehensive_tests():

    calculator = Calculator()

    # Тесты на правильные выражения
    correct_cases = [
        ("2+3", 5),
        ("10-4", 6),
        ("3*4", 12),
        ("15/3", 5),
        ("2+3*4", 14),
        ("(2+3)*4", 20),
        ("-5+3", -2),
        ("3.5+2.5", 6.0),
        ("10/2*3", 15),
        ("-(-3)", 3),
        ("0.5*2", 1.0),
    ]

    # Тесты на выражения с ошибками
    error_cases = [
        "2+*3",
        "3*/4",
        "*5",
        "5+",
        "3++4",
        "3..4",
        "2 + 3a",
        "(2+3",
        "2+3)",
        "2(*3)",
        "3(4)",
        "2)3",
        ")(",
        "",
        "5 / 0",
        "1.2.3",
        "123.",
    ]

    print("ТЕСТИРОВАНИЕ КОРРЕКТНЫХ ВЫРАЖЕНИЙ:")
    print("=" * 50)

    all_passed = True
    for expression, expected in correct_cases:
        try:
            result = calculator.calculate(expression)

            if abs(result - expected) < 0.000001:
                status = "PASS"
            else:
                status = "FAIL"
            print(f"{expression:15} = {result:8} (ожидается: {expected:8}) [{status}]")

            if status == "FAIL":
                all_passed = False

        except Exception as e:
            print(f"{expression:15} = ОШИБКА: {e} [FAIL]")
            all_passed = False

    print("\nТЕСТИРОВАНИЕ ОШИБОЧНЫХ ВЫРАЖЕНИЙ:")
    print("=" * 50)

    for expression in error_cases:
        try:
            result = calculator.calculate(expression)
            print(f"{expression:15} = {result:8} [FAIL - ожидалась ошибка]")
            all_passed = False
        except Exception as e:
            print(f"{expression:15} = ОШИБКА: {e} [PASS]")

    print("=" * 50)
    if all_passed:
        print("Результат: Все тесты пройдены!")
    else:
        print("Результат: Есть ошибки!")

    return all_passed