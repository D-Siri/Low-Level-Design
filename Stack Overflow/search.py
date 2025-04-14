from abc import ABC, abstractmethod

from enum import Enum


class SearchStrategy(Enum):
    KEYWORD = 1
    USERID = 2
    TAG = 3


class Search(ABC):
    @abstractmethod
    def search(self, query, questions):
        pass


class SearchByKeyword(Search):

    def search(self, query, questions):
        result = []
        for user_id, user_questions in questions.items():
            for user_question in user_questions:
                if query in user_question.get_content():
                    result.append(user_question)
        return result


class SearchByTag(Search):

    def search(self, query, questions):
        result = []
        for user_id, user_questions in questions.items():
            for user_question in user_questions:
                if query in user_question.get_tags():
                    result.append(user_question)
        return result


class SearchByUserId(Search):

    def search(self, query, questions):
        return questions[query]


class SearchFactory:
    @staticmethod
    def fetch_searcher(search_strategy):
        if search_strategy == SearchStrategy.TAG:
            return SearchByTag()
        elif search_strategy == SearchStrategy.KEYWORD:
            return SearchByKeyword()
        elif search_strategy == SearchStrategy.USERID:
            return SearchByUserId()
        else:
            print(f"Select appropriate search strategy")
