from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Magazine(models.Model):
    name = models.CharField(max_length=20)

    creator = models.ForeignKey(User)

    mods = models.ManyToManyField(User, related_name="mods")

    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    link = models.URLField(max_length=200)

    name = models.CharField(max_length=100, default="Lorem Ipsum")

    submitted_by = models.ForeignKey(User)

    submitted_to = models.ForeignKey(Magazine)
    submitted_on = models.DateTimeField(auto_now=True)


class Subscription(models.Model):
    subscribed_to = models.ForeignKey(Magazine)
    subscriber = models.ForeignKey(User)

    subscribed_date = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    article_on = models.ForeignKey(Article)
    submitted_by = models.ForeignKey(User)
    text = models.CharField(max_length=1024)
    submitted_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
