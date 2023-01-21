from django.db import models
from django.utils.timezone import now


class Survey(models.Model):
    name = models.CharField(max_length=50)
    review = models.TextField()
    wishes = models.TextField(blank=True)
    gameidea = models.CharField(max_length=15)
    gamedesign = models.CharField(max_length=15)
    gameplay = models.CharField(max_length=15)
    website = models.CharField(max_length=15)
    timestamp = models.DateTimeField(blank=True, default=now)

    class Meta:
        ordering = ['timestamp']
        verbose_name = 'Survey'
        verbose_name_plural = 'Surveys'

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name + ' / ' + self.review


class Question(models.Model):
    category = models.CharField(max_length=15, default='Project & Management')
    question = models.TextField()
    timestamp = models.DateTimeField(blank=True, default=now)

    class Meta:
        ordering = ['timestamp']
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.question

    def __repr__(self):
        return self.category + ' / ' + self.question
