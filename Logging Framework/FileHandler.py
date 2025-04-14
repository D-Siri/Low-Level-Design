from logger import Logger


class FileLogger(Logger):

    def __init__(self, path, level, content):
        super().__init__(level, content)
        self.path = path

    def write(self, content):
        with open(self.path, "a") as file:
            file.write(str(content) + "/n")
