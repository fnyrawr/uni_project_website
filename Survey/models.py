from django.db import models
from django.utils.timezone import now


RATING_CHOICES = [
        ('1', 'Meh'),
        ('2', 'Lame'),
        ('3', 'Mid'),
        ('4', 'Good'),
        ('5', 'Awesome'),
    ]


CATEGORY_CHOICES = [
        ('1', 'Project & Management'),
        ('2', 'Mechanics'),
        ('3', 'Multiplayer'),
        ('4', 'Assets, UI & Audio'),
        ('5', 'Website'),
    ]


class Survey(models.Model):
    name = models.CharField(max_length=50)
    review = models.TextField()
    wishes = models.TextField(blank=True)
    gameidea = models.CharField(
        max_length=1,
        choices=RATING_CHOICES,
        default=3,
    )
    gamedesign = models.CharField(
        max_length=1,
        choices=RATING_CHOICES,
        default=3,
    )
    gameplay = models.CharField(
        max_length=1,
        choices=RATING_CHOICES,
        default=3,
        blank=True
    )
    websiteDesign = models.CharField(
        max_length=1,
        choices=RATING_CHOICES,
        default=3,
    )
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
    category = models.CharField(
        max_length=1,
        choices=RATING_CHOICES,
    )
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
