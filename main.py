from itertools import chain
from log_dec import logger, param_logger

# Написать итератор, который принимает список списков, и возвращает их плоское представление,
# т.е последовательность состоящую из вложенных элементов

nested_list = [
    ["a", "b", "c"],
    ["d", "e", "f", "h", False],
    [1, 2, None],
]


class Flat_iterator:
    def __init__(self, nested_list):
        self.start = -1
        self.end = len(nested_list)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        return self

    # reassigning "__str__" method to print out the result of itteration el by el
    @param_logger("log\param_log_file.log")
    def __str__(self):
        return "\n".join(str(el) for el in nested_list[self.start])

    # method to print out the "unpacked" nested list as a single list of all elements
    @param_logger("log\param_log_file.log")
    def chain_list(nested_list):
        print(list(chain.from_iterable(nested_list)))


# Написать генератор, который принимает список списков, и возвращает их плоское представление
class Flat_generator:
    @param_logger("log\param_log_file.log")
    def flat_generator(self, nested_list):
        return [num for el in nested_list for num in el]


# Дополнительное задание: *аписать генератор, обрабатывающий списки с любым уровнем вложенности
nested_list2 = [
    ["a", "b", "c"],
    ["d", "e", "f", "h", False],
    [1, 2, None, [1, 2, 3, 4, 5, [True, None, False]]],
]


@logger
def flat_generator(nested_list2):
    for el in chain(nested_list2):
        if isinstance(el, list):
            yield from flat_generator(el)
        else:
            yield el


if __name__ == "__main__":
    # printing "unpacked" nested list element by element
    print("Печатаем каждый элемент вложенного списка списков")
    for elem in Flat_iterator(nested_list):
        print(elem)

    print("--------------------------------------------")

    # printing "unpacked" nested list in a single list of all elements
    print("Печатаем элементы вложенного списка списков в один список")
    Flat_iterator.chain_list(nested_list)

    print("--------------------------------------------")

    # printing generated elements from nested list one by one
    print("Генератор элементоы вложенного списка списков")
    result = Flat_generator()
    for el in result.flat_generator(nested_list):
        print(el)

    print("------------------------------------------------")

    # printing generated elements from multiple-layered nested list
    print("Генератор элементов из списка списков любого уровня вложенности")
    flat_list = [item for item in flat_generator(nested_list2)]
    for el in flat_list:
        print(el)

    print()
