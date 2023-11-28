#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def process_list(input_list, a, b):
    max_element = max(input_list)
    print("Максимальный элемент списка:", max_element)

    last_positive_index = -1
    for i in range(len(input_list) - 1, -1, -1):
        if input_list[i] > 0:
            last_positive_index = i
            break

    sum_before_last_positive = sum(input_list[:last_positive_index])
    print("Сумма элементов до последнего положительного элемента:", sum_before_last_positive)

    input_list = [x for x in input_list if abs(x) < a or abs(x) > b]

    input_list.extend([0] * (len(input_list) - last_positive_index - 1))

    return input_list

if __name__ == "__main__":
    my_list = [3, -7, 2, -1, 8, -4, 5, -6, 9, -2]
    a_value = 2
    b_value = 6

    result_list = process_list(my_list, a_value, b_value)
    print("Итоговый список:", result_list)
