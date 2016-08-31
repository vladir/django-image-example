from __future__ import unicode_literals

from django.db import models


class Partner(models.Model):
    logo = models.ImageField(upload_to='logo')

    def __str__(self):
        return self.logo.url
