# How can you make this more scalable and reusable later?
import functools

def find_armstrong_numbers(numbers):
    ans_list = []

    for single_num in numbers:
        split_num = (list(map(int,str(single_num))))
        summ_of_powers = 0

        for index_num in split_num:
            powers = index_num ** len(split_num)
            summ_of_powers += powers
            
        if summ_of_powers == single_num:
            ans_list.append(summ_of_powers)

    return ans_list
            


