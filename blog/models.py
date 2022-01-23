from datetime import datetime
from pyexpat import model
from unicodedata import category

from django.db import models
from django.utils.translation import gettext as _

from ckeditor.fields import RichTextField

class Article(models.Model):

    class ArticleVisibility(models.TextChoices):
        YES = 'Y', _('Yes')
        NO = 'N', _('No')

    title = models.CharField(max_length=255)
    author =  models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    category  = models.ForeignKey(
        'Category', 
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    body = RichTextField()
    visibility = models.CharField(max_length=1, choices=ArticleVisibility.choices, default=ArticleVisibility.NO)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.title

class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.category




