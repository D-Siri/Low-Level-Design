from abc import ABC, abstractmethod


class DocumentState(ABC):
    def __init__(self, document):
        self.document = document

    @abstractmethod
    def review_document(self):
        pass

    @abstractmethod
    def edit_document(self):
        pass

    @abstractmethod
    def publish_document(self):
        pass

    @abstractmethod
    def submit_to_review(self):
        pass
