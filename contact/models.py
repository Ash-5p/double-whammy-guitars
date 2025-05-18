from django.db import models


class Contact(models.Model):
    """
    Stores a single contact request
    """
    name = models.CharField(blank=False, max_length=200)
    email = models.EmailField(blank=False)
    message = models.TextField(blank=False)
    sent_on = models.DateTimeField(auto_now=True)
