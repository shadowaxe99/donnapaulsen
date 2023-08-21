class DraftManager:
    def __init__(self):
        self.drafts = []

    def create_draft(self, response):
        print(f'Creating draft for response: {response}')
        self.drafts.append(response)

    def get_drafts_to_send(self):
        return self.drafts