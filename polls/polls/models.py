from django.db import models
from django.utils import timezone

from django.contrib import admin

from datetime import timedelta


class Question(models.Model):
    question_text = models.TextField(max_length=200)
    published_date = models.DateTimeField()

    def __str__(self):
        return f"id:{self.id} | {self.question_text}"

    @admin.display(boolean = True)

    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.published_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"id:{self.id} | {self.choice_text}"
