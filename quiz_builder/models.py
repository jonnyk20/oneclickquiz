from django.db import models
from django.contrib.postgres.fields.jsonb import JSONField
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date


def defaultJSON():
    return {}


class QuizType(models.Model):
    description = models.CharField(max_length=200, blank=False)


class Quiz(models.Model):
    date_created = models.DateTimeField(
        'date created', blank=False, default=date.today)
    quiz_type = models.ForeignKey(
        QuizType, on_delete=models.CASCADE, blank=False)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, blank=False)
    correct_answer = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(3)], blank=False)


class ItemType(models.Model):
    description = models.CharField(max_length=200, blank=False)


class Item(models.Model):
    item_type = models.ForeignKey(
        ItemType, on_delete=models.CASCADE, blank=False)
    data = JSONField("data", default=defaultJSON, blank=False)


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, blank=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=False)
