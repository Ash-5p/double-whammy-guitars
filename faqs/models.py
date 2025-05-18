from django.db import models


class FAQ(models.Model):
    """
    Stores a single FAQ entry
    """
    question = models.TextField(blank=False)
    answer = models.TextField(blank=False)
    updated_on = models.DateTimeField(auto_now=True)
