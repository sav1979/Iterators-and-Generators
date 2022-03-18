# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 11:51:42 2022

@author: sklad_2
"""

# Написать генератор, который принимает список списков, и возвращает их плоское представление.
investment_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, ['noiwenf', 4,6,7, 9648498], 2, None],
]

flat_list = []

def my_generator(lists):
	for i in range(len(lists)):
		if type(lists[i]) == list:
			my_list = my_generator(lists[i])
			for i in my_list:
				yield i
		else:
			yield lists[i]

for item in  my_generator(investment_list):
	print(item, end=' ')
