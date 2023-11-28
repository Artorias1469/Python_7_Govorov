#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    pass

A = []

for i in range(10):
    element = float(input(f"Введите элемент {i + 1}: "))
    A.append(element)

sum_selected_elements = 0

for x in A:
    if 3 < x < 8:
        sum_selected_elements += x

print(f"Сумма элементов, больших 3 и меньших 8: {sum_selected_elements}")

if __name__ == "__main__":
    pass
