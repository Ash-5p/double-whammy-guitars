from django.db import models


class Newsletter(models.Model):
    """
    Stores a single newsletter subscription
    """
    email = models.EmailField(blank=False, unique=True)

    class Meta:
        verbose_name_plural = 'Newsletter Subscribers'
