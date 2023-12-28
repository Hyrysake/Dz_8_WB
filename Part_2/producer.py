from mongoengine import connect, Document, StringField, BooleanField
from faker import Faker
import json

fake = Faker()

class Contact(Document):
    full_name = StringField(required=True)
    email = StringField(required=True)
    message_sent = BooleanField(default=False)

uri = "mongodb+srv://Nazar:NazarCanon09@wb8.3wglwy9.mongodb.net/?retryWrites=true&w=majority"
connect(host=uri)

def send_email(contact_id):
    print(f"Email sent to contact with ID: {contact_id}")
    contact = Contact.objects.get(id=contact_id)
    contact.message_sent = True
    contact.save()


fake_contacts = []
for _ in range(10):
    contact = Contact(full_name=fake.name(), email=fake.email())
    contact.save()
    fake_contacts.append(str(contact.id))


for contact_id in fake_contacts:
    message = {'contact_id': contact_id}
    send_email(contact_id)
    print(f"Message sent for contact with ID: {contact_id}")
