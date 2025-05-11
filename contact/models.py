from django.db import models


class Contact(models.Model):
    name = models.CharField(blank=False, max_length=200)
    email = models.EmailField(blank=False)
    message = models.TextField(blank=False)
