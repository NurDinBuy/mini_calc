import numexpr
while True:
    try:
        expr = input('Введите математическое выражение: ')
        if expr == 'EXIT':
            print('Завершение цикла!')
            break
        result = numexpr.evaluate(expr)
        print(f'Результат: {result}')
    except Exception:
        print('Вводите числа!')