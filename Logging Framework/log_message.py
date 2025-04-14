import datetime


class Message:
    def __init__(self, content):
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.content = content
