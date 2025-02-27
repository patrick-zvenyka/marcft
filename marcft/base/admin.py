from django.contrib import admin
from .models import Post
from ckeditor.widgets import CKEditorWidget
from django.db import models
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }

admin.site.register(Post, PostAdmin)