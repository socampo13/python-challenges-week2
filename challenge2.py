## 🧩 **Challenge 2: List Comprehensions**
##* Write a function to transpose a 2D list (matrix) using a single list comprehension.
##* Expected function: `transpose(matrix: list[list[int]]) -> list[list[int]]`.



def transpose(matrix: list[list[int]]) -> list[list[int]]:
    if not matrix or not matrix[0]:
        raise ValueError("Matrix is empty or has emtpy rows")
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

## Test
if __name__ == "__main__":
    matrix = [
        [3, 2, 1],
        [4, 5, 6],
        [9, 8, 7]
    ]
    print(transpose(matrix))