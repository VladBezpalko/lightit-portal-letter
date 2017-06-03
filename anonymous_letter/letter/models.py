from django.db import models


class Letter(models.Model):
    text = models.TextField()
    response = models.TextField()
    codeword = models.CharField(max_length=128)
