from fizzbuzz import FizzBuzz

if __name__ == '__main__':
    o = FizzBuzz()

    expected = o.run('by_cheating')

    all_methods = [
        'by_cheating',
        'by_expression',
        'by_decode',
        'by_accumulator',
        'by_mapping',
        'by_tables',
        'by_boolean_multiplication',
        'by_lambda_decode',
        'by_functions',
        'by_framework',
    ]

    for method in all_methods:
        print(method, '=>', o.run(method) == expected)

    gen = o.generators()
    print('by_generators', '=>', [next(gen) for _ in range(100)] == expected)

# last line of code
