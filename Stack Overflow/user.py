import uuid


class User:

    def __init__(self, first_name, last_name):
        self.user_id = uuid.uuid1()
        self.score = 0
        self.first_name = first_name
        self.last_name = last_name

    def get_user_id(self):
        return self.user_id

    def add_score(self, score=1):
        self.score += score

    def get_name(self):
        return self.first_name + ', ' + self.last_name

    def __repr__(self):
        return f'User: {self.get_name()} with Score: {self.score}'
