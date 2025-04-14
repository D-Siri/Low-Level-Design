from abc import ABC, abstractmethod


class Votable(ABC):
    def __init__(self):
        self.votes = 0

    def up_vote(self):
        self.votes += 1

    def down_vote(self):
        self.votes -= 1

    @abstractmethod
    def get_id(self):
        pass
