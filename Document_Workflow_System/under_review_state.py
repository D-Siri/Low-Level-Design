from reviewer import Reviewer
from document_state import DocumentState


class UnderReview(DocumentState):

    def review_document(self):
        if Reviewer.review(self.document):
            self.document.set_state(self.document.publish_state)
            print("You can now publish the document")
        else:
            print("Review failed, Try again!")
            self.document.set_state(self.document.draft_state)

    def edit_document(self):
        print("Cannot edit the document in review state")

    def submit_to_review(self):
        self.document.set_state(self.document.review_state)
        print("Document not edited, cannot submit the same file again")

    def publish_document(self):
        print("Cannot Publish the document in Draft State")
