from log_handler import LogHandler


class ConsoleHandler(LogHandler):

    def write(self, message):
        print(f"message logged to console")
