from mongoengine import connect, Document, StringField, BooleanField
from bson import ObjectId
import json

uri = "mongodb+srv://Nazar:NazarCanon09@wb8.3wglwy9.mongodb.net/?retryWrites=true&w=majority"
connect(host=uri)

class Contact(Document):
    full_name = StringField(required=True)
    email = StringField(required=True)
    message_sent = BooleanField(default=False)

def take_user(user_id):
    contact = Contact.objects.get(id=user_id)
    contact.message_sent = True
    contact.save()
    print(f"Processed message for contact with ID: {user_id}")

def main():
    fake_contacts = Contact.objects(message_sent=False)
    for contact in fake_contacts:
        take_user(contact.id)

if __name__ == "__main__":
    main()
