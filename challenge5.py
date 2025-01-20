### 🧮 **Challenge 5: itertools**
##* Use `itertools.combinations` to find all unique combinations of size 3 from a list of numbers and return them as tuples.
##* Expected function: `find_combinations(nums: list[int]) -> list[tuple[int, int, int]]`.

from itertools import combinations

def find_combinations(nums: list[int]) -> list[tuple[int, int, int]]:
    if len(nums) < 3:
        raise ValueError("Input list must have min 3 numbers")
    
    return list(combinations(nums, 3))

## Test
if __name__ == "__main__":
    numbers = [4, 7, 2, 9]
    print(find_combinations(numbers))