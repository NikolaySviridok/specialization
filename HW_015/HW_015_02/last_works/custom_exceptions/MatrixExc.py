class MatrixExc(Exception):
    def __init__(self, name: str, message: str):
        self.name = name
        self.message = message

    def __str__(self):
        return f'AN ERROR OCCURRED. {self.name}: {self.message}'


class ConsistencyMatrixError(MatrixExc):
    def __init__(self, err_key: str = None):
        if err_key is None:
            super(ConsistencyMatrixError, self).__init__('Inconsistent Matrix Error',
                                                         "All rows must be of same length, "
                                                         "all values must be of types 'int' or 'float'")
        elif err_key == 'rows':
            super(ConsistencyMatrixError, self).__init__('Inconsistent Matrix Error',
                                                         'All rows must be of same length')
        elif err_key == 'values':
            super(ConsistencyMatrixError, self).__init__('Inconsistent Matrix Error',
                                                         "All values must be of types 'int' or 'float'")


class MatrixTypeError(MatrixExc):
    def __init__(self, value):
        super(MatrixTypeError, self).__init__('TypeError',
                                              f"{value} is not a 'Matrix' instance")


class MatrixValueError(MatrixExc):
    def __init__(self, value=None):
        if value is None:
            super(MatrixValueError, self).__init__('MatrixValueError',
                                                   "Operation not permitted for "
                                                   "different-dimensional matrices")
        else:
            super(MatrixValueError, self).__init__('MatrixValueError',
                                                   f"Unsupported operation between '{type(value)}'"
                                                   f"and 'Matrix'")


class MatrixMultiplyError(MatrixExc):
    def __init__(self):
        super(MatrixMultiplyError, self).__init__('MatrixMultiplyError',
                                                  "Operation not permitted if rows amount of first matrix "
                                                  "is not equal to columns amount of other one")