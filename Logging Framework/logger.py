from logger import Logger


class LogConfig:
    def __init__(self, log_level, logger):
        self.log_level = log_level
        self.logger = logger

    def set_log_level(self, log_level):
        self.log_level = log_level

    def get_log_level(self):
        return self.log_level

    def set_logger(self, logger):
        self.logger = logger

    def get_logger(self):
        return self.logger
