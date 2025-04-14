
from log_message import LogMessage


class Logger:
    def __init__(self):
        self.handler = None

    def set_handler(self, handler):
        self.handler = handler

    def log(self, level, message):
        message = LogMessage(message, level)
        if self.handler:
            self.handler.handle(message)




