from log_handler import LogHandler


class FileHandler(LogHandler):

    def __init__(self, path, level):
        super().__init__(level)
        self.path = path

    def write(self, message):
        with open(self.path, "a") as file:
            file.write(f"{message.timestamp} - {message.log_level} - {message.content}\n")
            print(f"message appended to file {self.path}")
