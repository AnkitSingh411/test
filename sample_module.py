"""Small sample module with ordinary helper functions."""


def greet(name):
    return f"Hello, {name}!"


def add_numbers(a, b):
    return a + b


def average(values):
    if not values:
        return 0
    total = 0
    for value in values:
        total += value
    return total / len(values)


def find_largest(values):
    largest = values[0]
    for value in values[1:]:
        if value > largest:
            largest = value
    return largest


def count_even(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count


def main():
    names = ["Asha", "Ravi", "Meera"]
    for name in names:
        print(greet(name))
    scores = [12, 25, 7, 30, 18]
    print("Total:", sum(scores))
    print("Average:", average(scores))
    print("Largest:", find_largest(scores))
    print("Even count:", count_even(scores))


if __name__ == "__main__":
    main()
