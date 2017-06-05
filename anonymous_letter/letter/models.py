from django.contrib.auth.hashers import check_password, make_password
from django.db import models

from letter.managers import LetterManager


class Letter(models.Model):
    text = models.TextField()
    response = models.TextField(null=True, default=None)
    codeword = models.CharField(max_length=128)

    objects = LetterManager()

    def set_codeword(self, raw_codeword):
        self.codeword = make_password(raw_codeword)

    def check_codeword(self, raw_codeword):
        def setter(raw_codeword):
            self.set_codeword(raw_codeword)
            self.save(update_fields=['codeword'])

        return check_password(raw_codeword, self.codeword, setter)
