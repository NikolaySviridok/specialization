# Задание 1
# Напишите функцию для транспорирования матрицы.

import random

class Matrix:
    def __init__(self, rows: int, columns: int):
        self.rows = rows
        self.columns = columns
        self.matrix = Matrix.create_matrix(rows, columns)

    @staticmethod
    def create_matrix(count_rows: int, count_columns: int) -> list[list]:
        new_matrix = []
        for _ in range(count_rows):
            row = []
            for _ in range(count_columns):
                row.append(random.randint(0, 9))
            new_matrix.append(row)
        return new_matrix

    def transposition(self):
        for column in range(self.columns):
            new_row = []
            for row in range(self.rows):
                new_row.append(self.matrix[row][column])
            self.matrix.append(new_row)
        for _ in range(self.rows):
            self.matrix.pop(0)

    def __str__(self):
        output = ''
        for row in self.matrix:
            for item in row:
                output += f'{item:^3}'
            output += '\n'
        return output


rows, columns = map(int, input('Введите количество строк и столбцов через пробел: ').split())

matrix = Matrix(rows, columns)

print(matrix)
matrix.transposition()
print(matrix)
