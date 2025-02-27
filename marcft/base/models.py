from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField  # Import CKEditor field
# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, null=True, on_delete = models.CASCADE)
    title = models.CharField(max_length = 300,null=False)
    subject = models.ForeignKey(Topic, on_delete = models.SET_NULL, null=True)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
    



