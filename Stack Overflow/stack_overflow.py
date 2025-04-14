from collections import defaultdict
from Votable import Votable
from Question import Question
import uuid
from answer import Answer
from search import SearchFactory
from Commentable import Commentable
from comment import Comment


class StackOverflow:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.users = []
            cls._instance.questions = defaultdict(list)

        return cls._instance

    def post_question(self, user, content):
        q_id = uuid.uuid1()
        user_id = user.get_user_id()
        question = Question(q_id, user_id, content)
        self.add_question(question, user)
        user.add_score(1)
        print(f"{user_id} posted question {q_id}")
        return question

    def post_answer(self, question, user, content):
        ans_id = uuid.uuid1()
        user_id = user.get_user_id()
        q_id = question.get_id()
        answer = Answer(ans_id, user_id, q_id, content)
        question.add_answer(answer)
        print(f"{ans_id} posted by {user_id} for question {q_id}")
        user.add_score(1)
        return answer

    def comment_on(self, commentable: Commentable, user, content):
        commenting_on = commentable.get_id()
        user_id = user.get_user_id()
        comment = Comment(commenting_on, user_id, content)
        commentable.add_comment(comment)
        user.add_score(1)
        print(f" {user_id} commented on {commenting_on}")

    def up_vote(self, votable_obj: Votable):
        votable_obj.up_vote()
        print(f"Up voted for {votable_obj.get_id()}")

    def down_vote(self, votable_obj: Votable):
        votable_obj.down_vote()
        print(f"Down voted for {votable_obj.get_id()}")

    def search_on(self, query, search_strategy):
        searcher = SearchFactory.fetch_searcher(search_strategy)
        print(f"Searching...")
        return searcher.search(query, self.questions)

    def add_question(self, question, user):
        self.questions[user].append(question)
        print(f"{user.get_user_id()} Added question {question.get_id()}")

    def add_user(self, user):
        self.users.append(user)
