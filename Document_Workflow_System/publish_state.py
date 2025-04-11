from document_state import DocumentState


class PublishState(DocumentState):

    def publish_document(self):
        print("Published Document")
        return

    def edit_document(self):
        print("Cannot edit the document in publish state")

    def submit_to_review(self):
        self.document.set_state(self.document.review_state)
        print("cannot review the document in publish state")

    def review_document(self):
        print('Cannot Review the document in Draft State')

