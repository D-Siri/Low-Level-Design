import random


class Reviewer:

    def __init__(self, document):
        self.document = document

    def review(self):
        return random.choice([True, False])