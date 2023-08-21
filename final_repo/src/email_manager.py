class EmailManager:
    def __init__(self):
        self.emails = []

    def check_for_new_emails(self):
        new_emails = self.emails
        self.emails = []
        return new_emails