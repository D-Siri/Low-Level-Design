from Votable import Votable
from Commentable import Commentable


class Question(Votable, Commentable):
    def __init__(self, q_id, user_id, content, tags=None):
        Votable.__init__(self)
        Commentable.__init__(self)
        self.user_id = user_id
        self.q_id = q_id
        self.content = content
        self.answers = []

        if tags is None:
            self.tags = []
        else:
            self.tags = tags

    def get_tags(self):
        return self.tags

    def add_tag(self, tag):
        self.tags.append(tag)

    def get_user(self):
        return self.user_id

    def get_content(self):
        return self.content

    def update_content(self, content):
        self.content = content

    def get_id(self):
        return self.q_id

    def add_answer(self, answer):
        self.answers.append(answer)

    def __repr__(self):
        s = '-' * 20
        s += f'\nQuestion: {self.content}\n Votes: {self.votes}\n'

        for comment in self.comments:
            s += f'Comment: {comment.get_content()}\n'

        for answer in self.answers:
            s += f'Answer: {answer.get_content()}\n'
        return s








