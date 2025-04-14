from abc import ABC, abstractmethod
import datetime


class Logger(ABC):
    def __init__(self, level, content):
        self.level = level
        self.next_logger = None


    def set_next(self, next_logger):
        self.next_logger = next_logger

    def log(self, level, message):
        if level >= self.level:
            self.write(message)
        if self.next_logger:
            self.next_logger.log(level, message)

    @abstractmethod
    def write(self, content):
        pass
