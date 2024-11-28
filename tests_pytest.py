import pytest
from RSA import MathUtilities, PrimeGenerator, RSA  # Замените 'your_module' на имя вашего модуля


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
        with pytest.raises(Exception):
            RSA.execute(self.rsa, "123456789")

    def test_rsa_execute_non_numeric_message(self):
        with pytest.raises(Exception):
            RSA.execute(self.rsa, "abc")

    def test_rsa_execute_empty_message(self):
        with pytest.raises(Exception):
            RSA.execute(self.rsa, "")

    def test_generate_e(self):
        e = RSA.generate_e(self.rsa, 40)
        assert e is not None  # Проверка, что e не равно None
        assert MathUtilities.gcd(e, 40) == 1  # Проверка, что e взаимно просто с Fi

    def test_generate_e_zero_Fi(self):
        with pytest.raises(Exception):
            RSA.generate_e(self.rsa, 0)


# Запуск тестов
if __name__ == "__main__":
    pytest.main()
