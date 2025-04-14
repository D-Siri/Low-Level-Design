from logger import Logger
class ConsoleLogger(Logger):

    def write(self, content):
        print(content)