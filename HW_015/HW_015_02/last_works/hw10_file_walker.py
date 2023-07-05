import os


class FileLister:

    def __init__(self, start_path: str) -> None:
        self.start_path = start_path

    def list_files(self, file_ext: str, full_path: bool = True) -> [list[str], list[list[str]]]:
        """
        Assembly a list of files with certain extension to process
        :param full_path: bool -- return full file-path string or list [path, file-name]
        :param file_ext: str -- file-extension to look for
        :return: list[str] -- list of files abs-paths
        """
        result_lst = []
        for path_tlp in os.walk(self.start_path):
            for item in path_tlp[2]:
                if item.endswith(file_ext):
                    file_path = (os.path.join(path_tlp[0], item)
                                 if full_path
                                 else [path_tlp[0], item])
                    result_lst.append(file_path)
        return result_lst