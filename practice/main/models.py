from django.db import models


class Word(models.Model):
    english_word = models.CharField('english', max_length=50)
    russian_word = models.CharField('russian', max_length=50)

    def __str__(self):
        return self.english_word
