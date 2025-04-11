from document_state import DocumentState


class DraftState(DocumentState):

    def edit_document(self):
        print("Editing Document")

    def submit_to_review(self):
        self.document.set_state(self.document.review_state)
        print("Submitted document for review")

    def review_document(self):
        print('Cannot Review the document in Draft State')

    def publish_document(self):
        print("Cannot Publish the document in Draft State")
