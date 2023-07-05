class FileListerExc(Exception):
    def __init__(self, name, message):
        self.name = name
        self.message = message

    def __str__(self):
        return f'AN ERROR OCCURRED. {self.name}: {self.message}'


class FileListerObjectError(FileListerExc):
    def __init__(self):
        super(FileListerObjectError, self).__init__('FileListerObjectError',
                                                    "A 'FileLister' object missing")


class FileListerPathError(FileListerExc):
    def __init__(self):
        super(FileListerPathError, self).__init__('FileListerPathError',
                                                  "A path given does not exist")


class FileListerExtensionError(FileListerExc):
    def __init__(self):
        super(FileListerExtensionError, self).__init__('FileListerExtensionError',
                                                       "A file extension ('str'-type) missing")