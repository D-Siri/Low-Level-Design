from logger import Logger


class DatabaseLogger(Logger):

    def __init__(self, url, level, content):
        super().__init__(level, content)
        self.url = url

    def write(self, content):
        print(f"writing to database")
