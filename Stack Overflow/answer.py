from Votable import Votable
from Commentable import Commentable


class Answer(Commentable, Votable):

    def __init__(self, answer_id, user_id, q_id, content):
        Votable.__init__(self)
        Commentable.__init__(self)
        self.answer_id = answer_id
        self.content = content
        self.user_id = user_id
        self.q_id = q_id

    def get_content(self):
        return self.content

    def get_id(self):
        return self.answer_id

    def __repr__(self):
        s = '-' * 20
        s += f'\nAnswer: {self.content}\n Votes: {self.votes}\n'

        for comment in self.comments:
            s += f'Comment: {comment.get_content()}\n'
        return s





