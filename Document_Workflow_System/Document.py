from document_state import DocumentState
from draft_state import DraftState
from publish_state import PublishState
from under_review_state import UnderReview
class Document():

    def __init__(self):
        self.current_state = DraftState(self)
        self.draft_state = DraftState(self)
        self.publish_state = PublishState(self)
        self.review_state = UnderReview(self)

    def set_state(self, state: DocumentState):
        self.current_state = state

    def edit_document(self):
        self.current_state.edit_document()

    def submit_to_review(self):
        self.current_state.submit_to_review()

    def review_document(self):
        self.current_state.review_document()

    def publish_document(self):
        self.current_state.publish_document()


