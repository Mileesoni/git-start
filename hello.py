from typing import Iterable

# hello.py


def add_numbers_while(numbers: Iterable[float]) -> float:
    """Return the sum of numbers using a while loop."""
    nums = list(numbers)  # ensure we can index
    total = 0.0
    i = 0
    while i < len(nums):
        total += nums[i]
        i += 1
    return total

if __name__ == "__main__":
    # Example usage
    sample = [1, 2, 3.5, 4]
    print("sum:", add_numbers_while(sample))