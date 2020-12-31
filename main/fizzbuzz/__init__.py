"""
Ten common and less common methods for counting FizzBuzz.
"""
from functools import partial
from itertools import cycle, count
from typing import List, Iterator


class FizzBuzz:
    map = {3: 'Fizz', 5: 'Buzz'}
    fizzes = ['Fizz', '', '']
    buzzes = ['Buzz', '', '', '', '']
    encoding = [3, 0, 0, 1, 0, 2, 1, 0, 0, 1, 2, 0, 1, 0, 0]
    codepoints = ['', 'Fizz', 'Buzz', 'FizzBuzz']
    cheatsheet = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz',
                  '16', '17', 'Fizz', '19', 'Buzz', 'Fizz', '22', '23', 'Fizz', 'Buzz', '26', 'Fizz', '28', '29',
                  'FizzBuzz', '31', '32', 'Fizz', '34', 'Buzz', 'Fizz', '37', '38', 'Fizz', 'Buzz', '41', 'Fizz', '43',
                  '44', 'FizzBuzz', '46', '47', 'Fizz', '49', 'Buzz', 'Fizz', '52', '53', 'Fizz', 'Buzz', '56', 'Fizz',
                  '58', '59', 'FizzBuzz', '61', '62', 'Fizz', '64', 'Buzz', 'Fizz', '67', '68', 'Fizz', 'Buzz', '71',
                  'Fizz', '73', '74', 'FizzBuzz', '76', '77', 'Fizz', '79', 'Buzz', 'Fizz', '82', '83', 'Fizz', 'Buzz',
                  '86', 'Fizz', '88', '89', 'FizzBuzz', '91', '92', 'Fizz', '94', 'Buzz', 'Fizz', '97', '98', 'Fizz',
                  'Buzz']

    def by_cheating(self, num: int) -> str:
        """
        This is the only solution that might cause value errors.
        """
        return self.cheatsheet[num - 1]

    def by_expression(self, num: int) -> str:
        if 0 == num % 15:
            return 'FizzBuzz'
        elif 0 == num % 3:
            return 'Fizz'
        elif 0 == num % 5:
            return 'Buzz'
        else:
            return str(num)

    def by_decode(self, num: int) -> str:
        return self.codepoints[self.encoding[num % 15]] or str(num)

    def by_accumulator(self, num: int) -> str:
        answer = ''
        if 0 == num % 3:
            answer += 'Fizz'
        if 0 == num % 5:
            answer += 'Buzz'
        return answer if answer else str(num)

    def by_mapping(self, num: int) -> str:
        """
        Dictionaries are ordered by sequence of item insertion, since python 3.5;
        Using older versions of python may produce unexpected results.
        """
        return ''.join(s for m, s in self.map.items() if num % m == 0) or str(num)

    def by_tables(self, num: int) -> str:
        return self.fizzes[num % 3] + self.buzzes[num % 5] or str(num)

    def by_boolean_multiplication(self, num: int) -> str:
        """
        Python treats bool values as integers, automagically. Because 0 is "false-ish" and 1 is "true-ish" and
        vice versa.
        """
        return 'Fizz' * (num % 3 == 0) + 'Buzz' * (num % 5 == 0) or str(num)

    def by_lambda_decode(self, num: int) -> str:
        return (
            lambda: str(num),
            lambda: 'Fizz',
            lambda: 'Buzz',
            lambda: 'FizzBuzz'
        )[self.encoding[num % 15]]()

    def by_functions(self, num: int) -> str:
        """
        The generic replace() function can replace numbers by texts if num is divisible by divisor.
        partial() creates shortcuts around replace(), for the special cases fizz() and buzz().
        Python can then add the results (two strings), and, because '' is "false-ish", it can alternatively return
        the or-ed string representation of the given number.
        """

        def replace(divisor, text):
            return '' if num % divisor else text

        fizz = partial(replace, 3, 'Fizz')
        buzz = partial(replace, 5, 'Buzz')
        return fizz() + buzz() or str(num)

    def by_framework(self, num: int) -> str:
        """
        Can easily be extended to handle additional divisors.
        """

        def make(divisor, text, func):
            return func if num % divisor else lambda _dummy: text + func('')

        def fizz(x):
            return make(3, 'Fizz', x)

        def buzz(x):
            return make(5, 'Buzz', x)

        return fizz(buzz(lambda x: x))(str(num))

    def generators(self) -> Iterator:
        """
        This shows the superpower of generators in modern python.
        """
        infinite_fizz = cycle(['', '', 'Fizz'])
        infinite_buzz = cycle(['', '', '', '', 'Buzz'])
        infinite_words = (a + b for a, b in zip(infinite_fizz, infinite_buzz))
        infinite_numbers = (n for n in count(1))

        def decide(w, n):
            return str(n) if not len(w) else w

        fizzbuzz_ = (decide(w, n) for w, n in zip(infinite_words, infinite_numbers))
        yield from fizzbuzz_

    def default(self, *args, **kwargs):
        raise RuntimeWarning('unknown method:', args, kwargs)

    def run(self, method: str) -> List[str]:
        result = []
        for n in range(1, 101):
            result.append(getattr(self, method, self.default)(n))
        return result

# last line of code
