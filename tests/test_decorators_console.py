import pytest

from src.decorators import log


@log()
def example_function_console(x):
    """Функция для тестирования - деление числа 5 на переменную"""
    return 5 / x


def test_log_decorator_success_console(capsys):
    """Проверка вывода ошибки  'example_function ок' в лог-файле при успешном выполнении функции"""
    assert example_function_console(5) == 1
    captured_message = capsys.readouterr()
    assert "example_function_console ok\n\n" in captured_message.out


def test_log_decorator_zero_div_err_console(capsys):
    """Проверка вывода ошибки 'ZeroDivisionError' в консоль при делении на ноль"""
    with pytest.raises(ZeroDivisionError):
        example_function_console(0)
    captured_message = capsys.readouterr()
    assert "example_function_console error: division by zero. Inputs: (0,), {}\n\n" in captured_message.out


def test_log_decorator_type_err_console(capsys):
    """Проверка вывода ошибки  'TypeError' в консоль при делении на строковое значение"""
    with pytest.raises(TypeError):
        example_function_console("5")
    captured_message = capsys.readouterr()
    assert (
        "example_function_console error: unsupported operand type(s) for /: 'int' and 'str'. Inputs: ('5',), {}\n\n"
        in captured_message.out
    )
