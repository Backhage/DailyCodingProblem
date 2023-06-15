from collections import defaultdict
from random import random


def histogram_counts(start_state, probabilities, num_steps):
    # Create quick lookup probability dict.
    probability_dict = defaultdict(dict)
    for state_a, state_b, probability in probabilities:
        probability_dict[state_a][state_b] = probability

    # Run the chain and count the states.
    current_state = start_state
    count_histogram = defaultdict(int)

    for _ in range(num_steps):
        count_histogram[current_state] += 1
        rand_value = random()
        for next_state, probability in probability_dict[current_state].items():
            rand_value -= probability
            if rand_value <= 0:
                current_state = next_state
                break

    return count_histogram
