import os


class FileSystemApi:
    def __init__(self, root_folder):
        self.root_folder = root_folder

    def __str__(self):
        return f"FILE SYSTEM OPENED ON PATH '{self.root_folder}'"

    def mkdir(self, path):
        try:
            os.mkdir(f"{self.root_folder}/{path}")
        except BaseException as be:
            pass

    def touch(self, path):
        with open(f"{self.root_folder}/{path}", "w") as f_out:
            pass

    def append(self, path, line):
        with open(f"{self.root_folder}/{path}", "a") as f_out:
            f_out.write(f"{line}\n")

    def write(self, path, cnt):
        with open(f"{self.root_folder}/{path}", "w") as f_out:
            f_out.write(cnt)

    def read(self, path):
        with open(f"{self.root_folder}/{path}", "r") as f_in:
            return f_in.read()

    def incr(self, path):
        if os.path.exists(f"{self.root_folder}/{path}"):
            nb = int(self.read(path))
            self.write(path, str(nb + 1))
            return nb + 1
        else:
            self.write(path, "1")
            return 1

    def find(self, path, folder=None):
        if len(path) == 0:
            return folder
        if folder is None:
            folder = self.root_folder
        candidates = [c for c in sorted(os.listdir(folder)) if c.startswith(path[0])]
        if len(candidates) == 0:
            return None

        return self.find(path[1:], f"{folder}/{candidates[0]}")

    __repr__ = __str__
