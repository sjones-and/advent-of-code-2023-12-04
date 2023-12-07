#!/usr/bin/env python3

import os
from time import perf_counter_ns

def get_numbers(input):
    return set([int(value.strip()) for value in input.split(' ') if len(value)>0])

def answer(input_file):
    start = perf_counter_ns()
    with open(input_file, "r") as input:
        data = input.read().split('\n')

    data = [line.split(':')[1].split('|') for line in data]
    values = [len(set.intersection(get_numbers(value[0]), get_numbers(value[1]))) for value in data]
    answer = sum([pow(2, value - 1) for value in values if value > 0])
    end = perf_counter_ns()

    print(f'The answer is: {answer}')
    print(f'{((end-start)/1000000):.2f} milliseconds')

input_file = os.path.join(os.path.dirname(__file__), "input")
answer(input_file)
