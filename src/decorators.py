from typing import Any


def log(filename: str = "") -> Any:
    def decorator(d_function: Any) -> Any:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = d_function(*args, **kwargs)
                if filename:
                    with open(filename, "a") as log_file:
                        log_file.write(f"{d_function.__name__} ok\n")
                else:
                    print(f"{d_function.__name__} ok\n")
                return result
            except Exception as err:
                if filename:
                    with open(filename, "a") as log_file:
                        log_file.write(f"{d_function.__name__} error: {err}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{d_function.__name__} error: {err}. Inputs: {args}, {kwargs}\n")
                raise

        return wrapper

    return decorator
