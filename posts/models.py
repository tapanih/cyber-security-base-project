from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Post(models.Model):
    content = models.CharField(max_length=4096)
    date_created = models.DateTimeField(default=now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
