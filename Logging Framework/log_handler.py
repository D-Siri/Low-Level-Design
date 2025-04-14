from abc import ABC, abstractmethod


class LogHandler(ABC):
    def __init__(self, level):
        self.next_logger = None
        self.level = level

    def set_next(self, next_logger):
        self.next_logger = next_logger

    def handle(self, message):
        if message.get_message_level() >= self.level:
            self.write(message)
        if self.next_logger:
            self.next_logger.handle(message)

    @abstractmethod
    def write(self, content):
        pass
