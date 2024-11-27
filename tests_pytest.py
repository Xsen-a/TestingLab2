import pytest
from RSA import MathUtilities, PrimeGenerator, RSA  # Замените 'your_module' на имя вашего файла


# Аттестационное тестирование
def test_power_number():
    assert MathUtilities.power_number(2, 3) == 8
    assert MathUtilities.power_number(5, 0) == 1
    assert MathUtilities.power_number(3, 4) == 81


def test_power_number_module():
    assert MathUtilities.power_number_module(2, 3, 5) == 3
    assert MathUtilities.power_number_module(5, 0, 7) == 1
    assert MathUtilities.power_number_module(10, 3, 6) == 4


def test_gcd():
    assert MathUtilities.gcd(48, 18) == 6
    assert MathUtilities.gcd(101, 10) == 1
    assert MathUtilities.gcd(54, 24) == 6


def test_extended_euclid():
    x, y, gcd = MathUtilities.extended_euclid(30, 12)
    assert gcd == 6
    assert 30 * x + 12 * y == gcd


def test_is_prime():
    assert PrimeGenerator.is_prime(2) == True
    assert PrimeGenerator.is_prime(3) == True
    assert PrimeGenerator.is_prime(4) == False
    assert PrimeGenerator.is_prime(29) == True
    assert PrimeGenerator.is_prime(1) == False


# Блочное тестирование
def test_gen_simple_numbers():
    p, q = PrimeGenerator.gen_simple_numbers(100, 200)
    assert p != q
    assert PrimeGenerator.is_prime(p)
    assert PrimeGenerator.is_prime(q)


# Интеграционное тестирование
def test_rsa_integration():
    rsa = RSA()
    message_str = "123456"
    decoded_message = rsa.execute(message_str)

    # Проверяем, что расшифрованное сообщение соответствует исходному
    # Для этого нам нужно проверить, что результат равен исходному значению
    # Это может потребовать модификации RSA для возврата исходного сообщения
    assert decoded_message == int(message_str)  # Это будет работать, если RSA реализован правильно


if __name__ == "__main__":
    pytest.main()
