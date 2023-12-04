#!/usr/bin/env python3

import os

def get_numbers(input):
    return set([int(value.strip()) for value in input.split(' ') if len(value)>0])

def answer(input_file):
    with open(input_file, "r") as input:
        data = input.read().split('\n')
    card_win_count = {}
    card_count = {}
    for line in data:
        [card_id, card_data] = line.split(':')
        card_id = int(card_id[5:].strip())
        card_data = card_data.split('|')
        card_count[card_id] = 1
        card_win_count[card_id] = len(set.intersection(get_numbers(card_data[0]), get_numbers(card_data[1])))

    for i in sorted(card_count.keys()):
        win_count = card_win_count[i]
        held_count = card_count[i]
        for j in range(i + 1, i + 1 + win_count):
            card_count[j] += held_count

    answer = sum(card_count.values())

    print(f'The answer is: {answer}')

input_file = os.path.join(os.path.dirname(__file__), "input")
answer(input_file)
