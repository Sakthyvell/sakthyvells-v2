from django.db import models
from django.utils.translation import gettext_lazy as _


from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):

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
    body = RichTextUploadingField()
    visibility = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-updated_on']

    def __str__(self) -> str:
        return self.title

class Category(models.Model):
    category = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['category']

    def __str__(self) -> str:
        return self.category



