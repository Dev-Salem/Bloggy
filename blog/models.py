from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import ForeignKey, fields
from django.urls import reverse


class Blog(models.Model):
    created_at = fields.DateTimeField(auto_now_add=True)
    title = fields.CharField(max_length=500)
    body = fields.TextField(blank=True)
    author = ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def get_absolute_url(self):
        return reverse("blogs")

    def __str__(self):
        return self.title[:20]


class Comment(models.Model):
    author = ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="comments",
    )
    blog = ForeignKey(Blog, on_delete=models.CASCADE)
    body = fields.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse("blogs")

    def __str__(self):
        return self.body
