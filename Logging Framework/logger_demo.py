from ConsoleHandler import ConsoleHandler
from DatabaseHandler import DatabaseHandler
from FileHandler import FileHandler
from log_levels import LogLevels
from logger import Logger


class LoggerDemo:
    console_handler = ConsoleHandler(LogLevels.DEBUG)
    file_handler = FileHandler("logfile.txt", LogLevels.INFO)
    db_handler = DatabaseHandler("logs", LogLevels.ERROR)

    logger = Logger()
    logger.set_handler(console_handler)

    console_handler.set_next(file_handler)
    file_handler.set_next(db_handler)
    logger.log(LogLevels.DEBUG, "This is a debug message.")
    logger.log(LogLevels.INFO, "This is an info message.")
    logger.log(LogLevels.WARNING, "This is a warning message.")
    logger.log(LogLevels.ERROR, "An error has occurred!")
    logger.log(LogLevels.FATAL, "Fatal error encountered!")

