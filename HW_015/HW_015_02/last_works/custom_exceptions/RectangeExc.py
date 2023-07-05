class RectangleExc(Exception):
    def __init__(self, name: str, message: str):
        self.name = name
        self.message = message

    def __str__(self):
        return f'AN ERROR OCCURRED. {self.name}: {self.message}'


class RectangleTypeError(RectangleExc):
    def __init__(self, value=None):
        if value:
            super(RectangleTypeError, self).__init__('TypeError', f"'{value}' is not a 'Rectangle' instance")
        else:
            super(RectangleTypeError, self).__init__('TypeError', f"Need only a 'Rectangle' instances")


class RectangleValueError(RectangleExc):
    def __init__(self, value=None):
        if value is None:
            super(RectangleValueError, self).__init__('ValueError', 'Width and length values must be greater than zero')
        else:
            super(RectangleValueError, self).__init__('ValueError', f"The value '{value}' is irrelevant. "
                                                                    f"Only 'int' or 'float' values")