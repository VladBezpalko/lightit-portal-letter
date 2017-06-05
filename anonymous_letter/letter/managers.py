from django.db import models


class LetterManager(models.Manager):
    use_in_migrations = True

    def create_letter(self, text, codeword):
        letter = self.model(text=text)
        letter.set_codeword(codeword)
        letter.save(using=self._db)
        return letter

    def unanswered(self):
        return self.get_queryset().filter(response__isnull=True)
