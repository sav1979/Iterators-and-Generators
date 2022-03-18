# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 11:49:37 2022

@author: sklad_2
"""

# Написать итератор, который принимает список списков,
# и возвращает их плоское представление,
# т.е последовательность состоящую из вложенных элементов.
test_list = [
 ['a', 'b', 'c', [1, 2, 3]],
    'a',
 ['d', 'e', 'f', 'h', False],
 [1, 2, None],
]


# flat_list = [item for item in FlatIterator(nested_list)]

class FlatIterator:

    def __init__(self, investment_list):
        self.investment_list = investment_list
        self.index = -1
        self.inner_iterator = None

    def __iter__(self):
        return self


    def __next__(self):
        try:
            if self.inner_iterator  is not None:
                return self.inner_iterator.__next__()
        except StopIteration:
            self.inner_iterator = None

        self.index += 1
        if self.index == len(self.nested_list):
            raise StopIteration
        if type(self.nested_list[self.index]) == list:
            self.inner_iterator = FlatIterator(self.nested_list[self.index])
            return self.inner_iterator.__next__()
        else:
            return self.nested_list[self.index]


if __name__ == '__main__':
    for item in FlatIterator(test_list):
        print(item, end=' ')