class AccountManager:
    def __init__(self):
        self.drafts = []

    def send_draft(self, draft):
        print(f'Sending draft: {draft}')
        self.drafts.remove(draft)