import random


class MathUtilities:
    @staticmethod
    def power_number(base_number, exponent):
        if exponent < 0:
            raise ValueError("Показатель степени не может быть отрицательным.")

        result = 1
        while exponent > 0:
            if (exponent & 1) == 1:
                result *= base_number
                exponent -= 1
            base_number *= base_number
            exponent >>= 1
        return result

    @staticmethod
    def power_number_module(base_num, exponent, module):
        if module == 0:
            raise ZeroDivisionError("Модуль не может быть равным нулю.")

        result = 1
        base_num = base_num % module

        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base_num) % module
            exponent >>= 1
            base_num = (base_num * base_num) % module
        return result

    @staticmethod
    def gcd(a, b):
        if b == 0 and a == 0:
            raise ZeroDivisionError("Числа a и b не могут быть отрицательными.")
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def extended_euclid(a, n):
        if n == 0:
            return 1, 0, a
        x, y, gcd = MathUtilities.extended_euclid(n, a % n)
        return y, x - (a // n) * y, gcd


class PrimeGenerator:
    @staticmethod
    def is_prime(n, k=100):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False

        for _ in range(k):
            a = random.randint(2, n - 2)
            if MathUtilities.gcd(a, n) != 1:
                return False
            if MathUtilities.power_number_module(a, n - 1, n) != 1:
                return False
        return True

    @staticmethod
    def gen_simple_numbers(min_border, max_border):
        if min_border == max_border:
            raise Exception("Границы для генерации простых чисел не должны быть равны.")

        while True:
            p = random.randint(min_border, max_border)
            if PrimeGenerator.is_prime(p):
                q = random.randint(min_border, max_border)
                while not (PrimeGenerator.is_prime(q) and p != q):
                    q = random.randint(min_border, max_border)
                return p, q


class RSA:
    def execute(self, message_str):

        if not message_str.isdigit():
            raise Exception("Ваше расшифрованное сообщение состоит не только из цифр.")

        if int(message_str) > 33554432:
            raise ValueError("Ваше сообщение слишком длинное (> 33554432), могут возникнуть ошибки.")

        # Ограничение разрядности псевдослучайного числа
        min_border = MathUtilities.power_number(2, 12)
        max_border = MathUtilities.power_number(2, 13)

        big_integers = PrimeGenerator.gen_simple_numbers(min_border, max_border)
        print(f"p: {big_integers[0]}")
        print(f"q: {big_integers[1]}\n")

        n = big_integers[0] * big_integers[1]
        print(f"Криптомодуль n: {n}\n")

        # Fi(n) = (p-1)(q-1)
        Fi = (big_integers[0] - 1) * (big_integers[1] - 1)
        print(f"Функция Эйлера: {Fi}\n")

        # Небольшое число, взаимно простое с Fi - GCD = 1
        e = self.generate_e(Fi)
        print(f"Число e: {e}")

        # Число, обратное e
        d, _, _ = MathUtilities.extended_euclid(e, Fi)
        if d < 0:
            d += Fi
        print(f"Число d: {d}\n")

        open_key = (e, n)
        print(f"Открытый ключ: {open_key}")
        close_key = (d, n)
        print(f"Закрытый ключ: {close_key}\n")

        message_int = int(message_str)

        print("Добавление цифровой подписи... \nИспользую закрытый ключ.")
        message_encode = MathUtilities.power_number_module(message_int, d, n)
        print(f"Ваше сообщение с подписью: {message_encode}")

        print("Расшифрование цифровой подписи...\nИспользую открытый ключ.")
        message_decode = MathUtilities.power_number_module(message_encode, e, n)

        return message_decode

    def generate_e(self, Fi):
        if Fi == 0:
            raise Exception("Функция Эйлера не может быть равна 0.")

        e = random.randint(3, 1000)
        while MathUtilities.gcd(e, Fi) != 1:
            e += 1
        return e


def main():
    message_str = input("Введите ваше сообщение из цифр: ")
    rsa = RSA()
    message_decode = rsa.execute(message_str)
    print(f"Ваше расшифрованное сообщение: {message_decode}")


if __name__ == "__main__":
    main()
