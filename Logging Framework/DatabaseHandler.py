from log_handler import LogHandler


class DatabaseHandler(LogHandler):

    def __init__(self, url, level):
        super().__init__(level)
        self.url = url

    def write(self, content):
        print(f"message stored in database")
