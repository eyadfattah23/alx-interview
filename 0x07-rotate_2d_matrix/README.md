# Rotate 2D Matrix 


Resources:

    Python Official Documentation:
        Data Structures (list comprehensions, nested list comprehension)
        More on Lists

    GeeksforGeeks Articles:
        Inplace rotate square matrix by 90 degrees
        Transpose a matrix in Single line in Python

    TutorialsPoint:
        Python Lists for basics of list manipulation in Python.

By understanding these concepts and utilizing the provided resources, you will be able to approach the problem methodically, first transposing the matrix and then reversing each row to achieve a 90-degree clockwise rotation. This project not only tests your ability to manipulate 2D matrices but also challenges you to think about optimizing your solution to operate in-place, thus improving their problem-solving and algorithmic thinking skills in Python.




Given an `n x n` 2D matrix, rotate it 90 degrees clockwise.

* Prototype: `def rotate_2d_matrix(matrix):`
* Do not return anything. The matrix must be edited in-place.
* You can assume the matrix will have 2 dimensions and will not be empty.

```bash
jessevhedden$ cat main_0.py
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

jessevhedden$
jessevhedden$ ./main_0.py
[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]
jessevhedden$
```
