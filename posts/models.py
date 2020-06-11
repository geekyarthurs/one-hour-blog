from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.shortcuts import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    postedDate = models.DateTimeField(blank=True, default=now)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='author')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post", kwargs={"pk": self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comment',
                             default=1)
    writer = models.CharField(max_length=100)
    comment = models.TextField()
    postedDate = models.DateTimeField(blank=True, default=now)
