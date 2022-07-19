import functools
import datetime

# Написать декоратор - логгер. Он записывает в файл дату и время вызова функции,
# имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
def logger(func):
    """
    Creating logger in accordance to 1st task
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k} = {v!r}" for k, v in kwargs.items()]
        parameters = ", ".join(args_repr + kwargs_repr)
        result = func(*args, **kwargs)
        time = datetime.datetime.now()
        end_function = f"function:{func.__name__!r} with parameters: {parameters} was called at: {time} and returned {result!r}\n"
        with open("log\log_file.log", "a+") as file:
            file.write(end_function)
        return result

    return wrapper


#  Написать декоратор из п.1, но с параметром – путь к логам.
def param_logger(path):
    """
    Creating parameterized logger in accordance to 2nd task
    """

    def _param_logger(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k} = {v!r}" for k, v in kwargs.items()]
            parameters = ", ".join(args_repr + kwargs_repr)
            result = func(*args, **kwargs)
            time = datetime.datetime.now()
            end_function = f"function:{func.__name__!r} with parameters: {parameters} was called at: {time} and returned {result!r}\n"
            with open(path, "a+") as file:
                file.write(end_function)
            return result

        return wrapper

    return _param_logger


# ПРОВЕРЯЕМ ФУНКЦИОНАЛ
@param_logger("log\param_log_file.log")
def multiplier(arr):
    new_list = []
    for i in arr:
        new_list.append(i**2)
    return new_list


my_list = [2, 6, 45, 32, 43]
my_list2 = [2, 5, 4, 7, 4]
multiplier(my_list)
multiplier(my_list2)
