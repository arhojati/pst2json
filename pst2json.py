import mailbox
import email
import json

def extract_emails_from_mbox(mbox_file_path):
    mbox = mailbox.mbox(mbox_file_path)
    emails = []

    for message in mbox:
        if message.get_content_type() == 'text/plain':
            body = message.get_payload(decode=True)
        elif message.is_multipart():
            for part in message.get_payload():
                if part.get_content_type() == 'text/plain':
                    body = part.get_payload(decode=True)
                    break
        else:
            body = None

        if body is not None and isinstance(body, bytes):
            body = body.decode('utf-8', errors='ignore')  # Decode bytes to string

        email = {
            'date': message['date'],
            'sender': message['from'],
            'recipients': message['to'],
            'subject': message['subject'],
            'body': body,
        }
        emails.append(email)

    return emails

# Example usage
mbox_file_path = '/home/alireza/Dev/pst2text/zanan/Inbox/mbox'
emails = extract_emails_from_mbox(mbox_file_path)
# save emails as json
json_file_path = '/home/alireza/Dev/pst2text/emails.json'
with open(json_file_path, 'w') as json_file:
    json.dump(emails, json_file)