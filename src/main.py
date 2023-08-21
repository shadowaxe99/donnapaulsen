#!/usr/bin/env python3

import os
import sys
from account_manager import AccountManager
from draft_manager import DraftManager
from email_manager import EmailManager
from response_generator import ResponseGenerator


if __name__ == '__main__':
    account_manager = AccountManager()
    draft_manager = DraftManager()
    email_manager = EmailManager()
    response_generator = ResponseGenerator()

    # Main loop
    while True:
        # Check for new emails
        new_emails = email_manager.check_for_new_emails()

        # Process each email
        for email in new_emails:
            # Generate a response
            response = response_generator.generate_response(email)

            # Create a new draft
            draft_manager.create_draft(response)

        # Check for any drafts that need to be sent
        drafts_to_send = draft_manager.get_drafts_to_send()

        # Send each draft
        for draft in drafts_to_send:
            account_manager.send_draft(draft)

        # Wait for a while before checking for new emails again
        time.sleep(60)