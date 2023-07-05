import os
import logging

from homework_15.task02.last_works import FileLister
from homework_15.task02.last_works.custom_exceptions import (FileListerExtensionError,
                                                             FileListerObjectError,
                                                             FileListerPathError,)


class FileListerWorks:

    def __init__(self, dir_path) -> None:
        FORMAT = '{asctime} - {levelname}: {msg}'
        _file = 'FileSearch_working.log'
        logging.basicConfig(filename=_file, format=FORMAT, style='{',
                            filemode='a', level=logging.NOTSET)
        self._logger = logging.getLogger(__name__)

        if os.path.exists(dir_path):
            self._logger.info(f'Lister created for directory: {dir_path}')
            self._lister = FileLister(dir_path)
        else:
            self._logger.error(f'Wrong path: {dir_path}')
            raise FileListerPathError

    def list_dir(self, file_ext: str = None, full_path: bool = True):
        if not file_ext:
            self._logger.error(f'Extension is not passed to class')
            raise FileListerExtensionError
        self._logger.info(f'Returning files list for dir: {self._lister.start_path}; for files with "{file_ext}" extension')
        return self._lister.list_files(file_ext, full_path)