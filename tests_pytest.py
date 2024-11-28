import re

import pytest
from RSA import MathUtilities, PrimeGenerator, RSA


class TestMathUtilities:

    def test_power_number(self):
        assert MathUtilities.power_number(64, 5) == 1073741824
        assert MathUtilities.power_number(5, 0) == 1

    def test_power_number_negative(self):
        with pytest.raises(ValueError):
            MathUtilities.power_number(2, -3)

    def test_power_number_module(self):
        assert MathUtilities.power_number_module(5, 3, 13) == 8

    def test_power_number_module_zero_modulus(self):
        with pytest.raises(ZeroDivisionError):
            MathUtilities.power_number_module(4, 8, 0)

    def test_gcd(self):
        assert MathUtilities.gcd(48, 18) == 6

    def test_gcd_zero_zero(self):
        with pytest.raises(ZeroDivisionError):
            MathUtilities.gcd(0, 0)

    def test_math_utilities_extended_euclid(self):
        assert MathUtilities.extended_euclid(15, 0) == (1, 0, 15)
        assert MathUtilities.extended_euclid(0, 5) == (0, 1, 5)
        assert MathUtilities.extended_euclid(30, 12) == (1, -2, 6)


# Тесты для PrimeGenerator
class TestPrimeGenerator:

    def test_is_prime(self):
        assert PrimeGenerator.is_prime(7) is True
        assert PrimeGenerator.is_prime(4) is False
        assert PrimeGenerator.is_prime(1) is False

    def test_is_prime_negative(self):
        assert PrimeGenerator.is_prime(-5) is False

    def test_gen_simple_numbers(self):
        primes = PrimeGenerator.gen_simple_numbers(10, 50)
        assert len(primes) == 2  # Проверка, что вернулось два числа
        assert primes[0] != primes[1]  # Проверка, что числа разные

    def test_gen_simple_numbers_no_primes(self):
        with pytest.raises(Exception):
            PrimeGenerator.gen_simple_numbers(10, 10)


# Тесты для RSA
class TestRSA:
    rsa = RSA()

    def test_rsa_execute(self):
        assert RSA.execute(self.rsa, "12345") == 12345

    def test_rsa_execute_long(self):
        with pytest.raises(ValueError):
            RSA.execute(self.rsa, "123456789")

    def test_rsa_execute_non_numeric_message(self):
        with pytest.raises(Exception):
            RSA.execute(self.rsa, "abc")

    def test_rsa_execute_empty_message(self):
        with pytest.raises(Exception):
            RSA.execute(self.rsa, "")

    def test_generate_e(self):
        e = RSA.generate_e(self.rsa, 40)
        assert e is not None
        assert MathUtilities.gcd(e, 40) == 1

    def test_generate_e_zero_Fi(self):
        with pytest.raises(Exception):
            RSA.generate_e(self.rsa, 0)


class TestIntegration:
    def test_rsa_encrypt_decrypt_correct(self):
        rsa = RSA()
        messages = ["12345", "10004", "5"]

        for message in messages:
            decrypted_message = rsa.execute(message)
            assert decrypted_message == int(message)

    def test_prime_generator_generate_simple_numbers(self):
        prime_gen = PrimeGenerator()
        min_border = 4096
        max_border = 8192
        p, q = prime_gen.gen_simple_numbers(min_border, max_border)

        assert p != q
        assert prime_gen.is_prime(p)
        assert prime_gen.is_prime(q)

    def test_rsa_generate_e(self):
        rsa = RSA()
        fi = 314
        e_values = set()

        for _ in range(100):  # Генерируем e 100 раз
            e = rsa.generate_e(fi)
            e_values.add(e)

        assert len(e_values) > 1  # Проверяем, что сгенерировано несколько различных значений e

    def test_rsa_generate_e_zero_fi(self):
        rsa = RSA()

        with pytest.raises(Exception):
            rsa.generate_e(0)

    def test_math_utilities_extended_euclid(self):
        assert MathUtilities.extended_euclid(30, 12) == (1, -2, 6)
        assert MathUtilities.extended_euclid(15, 0) == (1, 0, 15)
        assert MathUtilities.extended_euclid(0, 5) == (0, 1, 5)

    def test_is_prime(self):
        prime_gen = PrimeGenerator()
        assert prime_gen.is_prime(7) is True
        assert prime_gen.is_prime(4) is False
        assert prime_gen.is_prime(1) is False

    def test_is_prime_negative(self):
        prime_gen = PrimeGenerator()
        assert prime_gen.is_prime(-5) is False

class TestAttest:
    def test_execute_valid_message(self, capfd):
        rsa = RSA()
        message_str = "12345"

        # Вызов метода
        message = rsa.execute(message_str)

        # Получаем вывод
        captured = capfd.readouterr()
        output = captured.out.splitlines()
        output = [s for s in output if s and s.strip()]

        expected_patterns = [
            r'p: \d{4}',
            r'q: \d{4}',
            r'Криптомодуль n: \d{8}',
            r'Функция Эйлера: \d{8}',
            r'Число e: \d+',
            r'Число d: \d+',
            r'Открытый ключ: \(\d+, \d+\)',
            r'Закрытый ключ: \(\d+, \d+\)',
            r'Добавление цифровой подписи\.\.\. ',
            r'Использую закрытый ключ\.',
            r'Ваше сообщение с подписью: \d+',
            r'Расшифрование цифровой подписи\.\.\.',
            r'Использую открытый ключ\.'
        ]

        for pattern in expected_patterns:
            assert any(re.match(pattern, line) for line in output)

        assert str(message) == message_str

    def test_execute_invalid_message(self):
        rsa = RSA()
        message_str = "abc"

        with pytest.raises(Exception) as excinfo:
            rsa.execute(message_str)

        assert str(excinfo.value) == "Ваше расшифрованное сообщение состоит не только из цифр."

    def test_execute_empty_message(self):
        rsa = RSA()
        message_str = ""

        with pytest.raises(Exception) as excinfo:
            rsa.execute(message_str)

        assert str(excinfo.value) == "Ваше расшифрованное сообщение состоит не только из цифр."

    def test_execute_too_large_message(self):
        rsa = RSA()
        message_str = "33554433"

        with pytest.raises(ValueError) as excinfo:
            rsa.execute(message_str)

        assert str(excinfo.value) == "Ваше сообщение слишком длинное (> 33554432), могут возникнуть ошибки."


if __name__ == "__main__":
    pytest.main()
