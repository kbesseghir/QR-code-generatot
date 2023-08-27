from django.db import models

from django.forms import Form, CharField

class QRCodeForm(Form):
    url = CharField(label='URL', max_length=255)
