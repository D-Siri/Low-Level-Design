import datetime


class LogMessage:
    def __init__(self, content, log_level):
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.content = content
        self.log_level = log_level

    def get_message_level(self):
        return self.log_level


