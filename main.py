import math
import random

def calculate_average(numbers):
    # Bug: no check for empty list (division by zero)
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total / len(numbers)


def find_max(numbers):
    # Bug: assumes list is non-empty
    max_num = 0  # Problem: fails for all-negative lists
    for n in numbers:
        if n > max_num:
            max_num = n
    return max_num


def process_data(data):
    result = []
    for i in range(len(data)):
        if type(data[i]) == int:  # Bad practice: use isinstance
            result.append(data[i] * 2)
        elif type(data[i]) == str:
            result.append(data[i].strip().lower())
        else:
            pass  # Silent failure
    return result


def random_sleep():
    # Suspicious / unnecessary randomness
    t = random.randint(1, 3)
    for i in range(t * 10000000):
        pass  # Wasteful CPU loop


def compute():
    data = [1, 2, -5, " Hello ", None]

    avg = calculate_average(data[:3])
    max_val = find_max(data[:3])
    processed = process_data(data)

    print("Average:", avg)
    print("Max:", max_val)
    print("Processed:", processed)

    random_sleep()


if __name__ == "__main__":
    compute()