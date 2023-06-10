#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if column == len(matrix[row]) - 1:
                print(matrix[row][column])
            else:
                print(matrix[row][column], end=" ")
    print()
