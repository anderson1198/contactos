from django.db import models
from django.db.models.fields import EmailField, TextField

# Create your models here.


class contacts (models.Model) :

    name_contact = TextField(max_length=30)
    phone_contact = TextField(max_length=10)
    email_contact = EmailField()

