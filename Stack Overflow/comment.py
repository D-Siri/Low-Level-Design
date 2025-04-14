import uuid


class Comment:
    def __init__(self, commenting_on, user_id, content):
        self.comment_id = uuid.uuid1()
        self.commenting_on = commenting_on
        self.user_id = user_id
        self.content = content

    def get_content(self):
        return self.content
