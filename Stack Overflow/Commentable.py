from abc import ABC, abstractmethod


class Commentable(ABC):
    def __init__(self):
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)

    @abstractmethod
    def get_id(self):
        pass
