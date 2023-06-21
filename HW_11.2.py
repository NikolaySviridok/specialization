# Задание 2
# Создайте класс Матрица. Добавьте методы для:
#   - вывода на печать,
#   - сравнения,
#   - сложения,
#   - *умножения матриц

class Matrix:
    _rows: int = None
    _cols: int = None
    _a_matrix: list[list[int, float]] = None

    def __init__(self, a_matrix: list[list[int, float]]) -> None:
        """
        Init matrix
        :param cols: int    -- a number of columns
        :param rows: int    -- a number of rows
        """
        self._rows = len(a_matrix)
        self._cols = len(a_matrix[0])
        self._a_matrix = a_matrix

    def __add__(self, other) -> 'Matrix':
        """
        Calculates a sum of matrices
        :param other: Matrix    -- other Matrix object
        :return: Matrix         -- new Matrix object
        """
        if not isinstance(other, self.__class__):
            raise TypeError("Not a 'Matrix'-type object")
        if self._rows != other._rows or self._cols != other._cols:
            raise ValueError("Operation not permitted for different-dimensional matrices")
        new_matrix = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        for j in range(self._rows):
            for i in range(self._cols):
                new_matrix[j][i] = self._a_matrix[j][i] + other._a_matrix[j][i]
        return Matrix(new_matrix)

    def __mul__(self, other) -> 'Matrix':
        """
        Calculates a multiplication of matrices or multiplication the matrix by a number
        :param other: [int, float, Matrix]    -- other Matrix object
        :return: Matrix                       -- new Matrix object
        """
        if isinstance(other, self.__class__):
            return self.__rmul__(other)
        elif isinstance(other, int) or isinstance(other, float):
            new_matrix = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
            for j in range(self._rows):
                for i in range(self._cols):
                    new_matrix[j][i] = self._a_matrix[j][i] * other
            return Matrix(new_matrix)
        else:
            raise TypeError("Unsupported operation")

    def __rmul__(self, other) -> 'Matrix':
        """
        Calculates a multiplication of matrices
        :param other: Matrix    -- other Matrix object
        :return: Matrix         -- new Matrix object
        """
        if not isinstance(other, self.__class__):
            raise TypeError("Not a 'Matrix'-type object")
        if self._cols != other._rows:
            raise ValueError("Operation not permitted if rows amount of first matrix "
                             "is not equal to columns amount of other one")
        new_matrix = [[0 for _ in range(other._rows)] for _ in range(self._rows)]
        for j in range(self._rows):
            for i in range(other._rows):
                new_matrix[j][i] = self._a_matrix[j][i] * other._a_matrix[i][j]
        return Matrix(new_matrix)

    def __eq__(self, other) -> bool:
        """Returns True if the matrix equals to other one"""
        if self is other:
            return True
        if not isinstance(other, self.__class__):
            raise TypeError("Not a 'Matrix'-type object")
        if self._rows != other._rows or self._cols != other._cols:
            return False
        for j in range(self._rows):
            for i in range(self._cols):
                if self._a_matrix[j][i] != other._a_matrix[j][i]:
                    return False
        return True

    def __ne__(self, other) -> bool:
        """Returns True if the matrix not equals to other"""
        return not self.__eq__(other)

    def __str__(self) -> str:
        """User-readable representation method"""
        return '\n'.join(['\t'.join(map(str, row)) for row in self._a_matrix]) + '\n'

    def __repr__(self):
        """String object representation method"""
        return f'Matrix({self._a_matrix})'


def main():
    mtx_a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    mtx_b = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    mtx_c = Matrix([[10, 11, 12], [4, 5, 6], [1, 2, 3], [7, 8, 9]])
    mtx_d = Matrix([[1, 2, 3, 4, ], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(repr(mtx_a))
    print(mtx_a)
    print(mtx_b)
    print(mtx_c)
    print(mtx_d)

    print(f'{mtx_a == mtx_b=}')
    print(f'{mtx_a == mtx_b=}')
    print(f'{mtx_b == mtx_c=}')
    print(f'{mtx_b != mtx_c=}')
    print(f'{mtx_c != mtx_d=}')
    print(mtx_a + mtx_b)
    print(mtx_a + mtx_c)
    try:
        print(mtx_c + mtx_d)
    except ValueError as exc:
        print(f'FAIL! {exc.__class__.__name__}: {exc}')
    try:
        print(mtx_a * mtx_b)
    except ValueError as exc:
        print(f'FAIL! {exc.__class__.__name__}: {exc}')
    try:
        print(mtx_a * mtx_d)
    except ValueError as exc:
        print(f'FAIL! {exc.__class__.__name__}: {exc}')
    try:
        print(mtx_a * 10)
    except TypeError as exc:
        print(f'FAIL! {exc.__class__.__name__}: {exc}')


if __name__ == '__main__':
    main()