# Блочные тесты #
| Класс          | Название                              | Описание                                                                                                               | Тип теста     | Входные данные                                                                   | Ожидаемый результат            |
|----------------|---------------------------------------|------------------------------------------------------------------------------------------------------------------------|---------------|----------------------------------------------------------------------------------|--------------------------------|
| MathUtilities  | test_power_number                     | Проверяет, что функция power_number правильно возводит число в степень                                                 | позитивный    | base_number = 64 <br/> exponent = 5 <br/><br/> base_number = 5 <br/> exponent = 0 | 1073741824 <br/> 1             |
| MathUtilities  | test_power_number_negative            | Проверяет, что функция power_number вызывает ошибку при отрицательном экспоненте                                       | негативный    | base_number = 2 <br/> exponent = -3                                              | Исключение (ValueError)        |
| MathUtilities  | test_power_number_module              | Проверяет, что функция power_number_module правильно работает с возведением в степень по модулю                        | позитивный    | base_num = 5 <br/> exponent = 3 <br/> module = 13                                | 8                              |
| MathUtilities  | test_power_number_module_zero_modulus | Проверяет, что функция power_number_module вызывает ошибку при модуле равном 0                                         | негативный    | base_num = 4 <br/> exponent = 8 <br/> module = 0                                 | Исключение (ZeroDivisionError) |
| MathUtilities  | test_gcd                              | Проверяет, что функция gcd правильно вычисляет наибольший общий делитель                                               | позитивный    | a = 48 <br/> b = 18                                                              | 6                              |
| MathUtilities  | test_gcd_zero_zero                    | Проверяет, что функция gcd вызывает ошибку при передаче двух нулей                                                     | негативный    | a = 0 <br/> b = 0                                                                | Исключение (ZeroDivisionError) |
| PrimeGenerator | test_is_prime                         | Проверяет, что функция is_prime правильно определяет простые числа                                                     | позитивный    | n = 7 <br/> n = 4 <br/> n = 1                                                    | True <br/> False <br/> False   |
| PrimeGenerator | test_is_prime_negative                | Проверяет, что функция is_prime возвращает False для отрицательных чисел                                               | негативный    | n = -5                                                                           | False                          |
| PrimeGenerator | test_gen_simple_numbers               | Проверяет, что функция gen_simple_numbers возвращает два различных простых числа                                       | позитивный    | min_border = 10 <br/> max_border = 50                                            | Два различных простых числа    |
| PrimeGenerator | test_gen_simple_numbers_no_primes     | Проверяет, что функция gen_simple_numbers вызывает ошибку при одинаковых границах                                      | негативный    | min_border = 10 <br/> max_border = 10                                            | Исключение (Exception)         |
| RSA            | test_rsa_execute                      | Проверяет, что функция execute правильно обрабатывает числовое сообщение                                               | позитивный    | message_str = "12345"                                                            | 12345                          |
| RSA            | test_rsa_execute_long                 | Проверяет, что функция execute вызывает ошибку при слишком большом сообщении (длиннее 8 знаков, больше чем 33554432)   | негативный    | message_str = "123456789"                                                        | Исключение (Exception)         |
| RSA            | test_rsa_execute_non_numeric_message  | Проверяет, что функция execute вызывает ошибку при нечисловом сообщении                                                | негативный    | message_str = "abc"                                                              | Исключение (Exception)         |
| RSA            | test_rsa_execute_empty_message        | Проверяет, что функция execute вызывает ошибку при пустом сообщении                                                    | негативный    | message_str = ""                                                                 | Исключение (Exception)         |
| RSA            | test_generate_e                       | Проверяет, что функция generate_e возвращает число, взаимно простое с Fi                                               | позитивный    | Fi = 40                                                                          | e (взаимно простое число)      |
| RSA            | test_generate_e_zero_Fi               | Проверяет, что функция generate_e вызывает ошибку при Fi = 0                                                           | негативный    | Fi = 0                                                                           | Исключение (Exception)         |
# Интеграционные тесты #
| Название                                     | Описание                                                                                                                                                 | Тип теста     | Входные данные                      | Ожидаемый результат               |
|----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|-------------------------------------|-----------------------------------|
| test_rsa_encrypt_decrypt_correct             | Проверяет успешное выполнение процесса шифрования и расшифрования сообщения функцией RSA.execute для разных сообщений.                                   | Позитивный    | message_str="12345", "10004", "5"   | 12345, 10004, 5                   |
| test_prime_generator_generate_simple_numbers | Проверяет, что функция PrimeGenerator.gen_simple_numbers каждый раз генерирует два различных простых числа в заданном диапазоне при нескольких запусках. | Позитивный    | min_border=4096, max_border=8192    | p != q и p, q - простые числа     |
| test_rsa_generate_e                          | Проверяет, что функция RSA.generate_e каждый раз генерирует разное число е, взаимно простое к функции Эйлера.                                            | Позитивный    | Fi = 314                            | е, различные                      |
| test_rsa_generate_e_zero_fi                  | Проверяет выброс исключения при передаче нуля в функцию generate_e класса RSA.                                                                           | Негативный    | Fi=0      	                         | Exception                         |
| test_math_utilities_extended_euclid          | Проверяет корректность работы расширенного алгоритма Евклида MathUtilities.extended_euclid, использующий MathUtilities.gcd.                              | Позитивный    | a, n = (30, 12), (15, 0), (0, 5)    | (1, -2, 6), (1, 0, 15), (0, 1, 5) |
| test_is_prime                                | Проверяет, что функция is_prime правильно определяет простые числа, используя методы MathUtilities.gcd, MathUtilities.power_number_module.               | Позитивный    | n = 7 <br/> n = 4 <br/> n = 1       | True <br/> False <br/> False      |
| test_is_prime_negative                       | Проверяет, что функция is_prime возвращает False для отрицательных чисел, используя методы MathUtilities.gcd, MathUtilities.power_number_module.         | Негативный    | n = -5                              | False                             |
# Аттестационные тесты #
| Название                       | Описание                                                                                                     | Тип теста  | Входные данные          | Ожидаемый результат                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------|--------------------------------------------------------------------------------------------------------------|------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| test_execute_valid_message     | Проверяет вывод в консоль значений в процессе шифрования и расшифрования и правильность ответа.              | Позитивный | message_str="12345"     | ['p: 7759', 'q: 5683', 'Криптомодуль n: 44094397', 'Функция Эйлера: 44080956', 'Число e: 731', 'Число d: 28402367', 'Открытый ключ: (731, 44094397)', 'Закрытый ключ: (28402367, 44094397)', 'Добавление цифровой подписи... ', 'Использую закрытый ключ.', 'Ваше сообщение с подписью: 16231577', 'Расшифрование цифровой подписи...', 'Использую открытый ключ.'], "12345" |
| test_execute_invalid_message   | Проверяет, что вывод в консоль содержит соответствующее не числовой строке сообщение об ошибке.              | Негативный | message_str="abc"       | "Ваше расшифрованное сообщение состоит не только из цифр."                                                                                                                                                                                                                                                                                                                   |
| test_execute_empty_message     | Проверяет, что вывод в консоль содержит соответствующее пустой строке сообщение об ошибке.                   | Негативный | message_str=""          | "Ваше расшифрованное сообщение состоит не только из цифр."                                                                                                                                                                                                                                                                                                                   |
| test_execute_too_large_message | Проверяет, что вывод в консоль содержит соответствующее слишком большому числу в строке сообщение об ошибке. | Негативный | message_str="33554433 " | "Ваше сообщение слишком длинное (> 33554432), могут возникнуть ошибки."                                                                                                                                                                                                                                                                                                                   |