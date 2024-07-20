import pytest

from src.decorators import log


@log("tests.txt")
def example_function(x):
    """Функция для тестирования - деление числа 5 на переменную"""
    return 5 / x


def test_log_decorator_zero_div_err():
    """Проверка вызова исключения 'ZeroDivisionError' при делении на ноль"""
    with pytest.raises(ZeroDivisionError):
        example_function(0)


def test_log_decorator_type_err():
    """Проверка вызова исключения 'TypeError' при делении на строковое значение"""
    with pytest.raises(TypeError):
        example_function("5")


def test_log_decorator_success_logging():
    """Проверка наличия записи 'example_function ок' в лог-файле при успешном выполнении функции"""
    assert example_function(5) == 1
    with open("tests.txt", "r", encoding="UTF-8") as log_file:
        lines = log_file.read()
        assert "example_function ok" in lines


def test_log_decorator_zero_div_err_logging():
    """Проверка наличия записи 'ZeroDivisionError' в лог-файле при делении на ноль"""
    with pytest.raises(ZeroDivisionError):
        example_function(0)
    with open("tests.txt", "r", encoding="UTF-8") as log_file:
        lines = log_file.read()
        assert "example_function error: division by zero. Inputs: (0,), {}" in lines


def test_log_decorator_type_err_logging():
    """Проверка наличия записи 'TypeError' в лог-файле при делении на строковое значение"""
    with pytest.raises(TypeError):
        example_function("5")
    with open("tests.txt", "r", encoding="UTF-8") as log_file:
        lines = log_file.read()
        assert (
            "example_function error: unsupported operand type(s) for /: 'int' and 'str'. Inputs: ('5',), {}" in lines
        )
