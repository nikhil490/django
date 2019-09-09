from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


types_list = [
    ('python', 'Python'),
    ('c', 'C/C++'),
    ('django', 'Django'),
    ]


class Article(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=120)
    types = models.CharField(max_length=6, choices=types_list, default='python')
    Content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    time_of_modification = models.DateTimeField(auto_now=True,auto_now_add=False)
    thumb = models.ImageField(upload_to="media/", default='default.jpg', blank=True)

    def __str__(self):
        return self.Title

    def snippet(self):
        return self.body[:50]


class Comment(models.Model):
    post = models.ForeignKey('Article', related_name='comments', on_delete = models.CASCADE)
    author = models.CharField(max_length=250)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text




