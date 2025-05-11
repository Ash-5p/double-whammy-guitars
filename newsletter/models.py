from django.db import models


class Newsletter(models.Model):
    email = models.EmailField(blank=False, unique=True)

    class Meta:
        verbose_name_plural = 'Newsletter Subscribers'
