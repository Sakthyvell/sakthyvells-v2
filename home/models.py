from statistics import mode
from django.db import models
from ckeditor.fields import RichTextField

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField(blank=True, null=True)
    url = models.URLField()
    image = models.ImageField()
    video = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title


class Work(models.Model):
    company = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    description = RichTextField(blank=True, null=True)
    started = models.DateField()
    ended = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return self.company + ' ' + self.role


class School(models.Model):
    name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    description = RichTextField(blank=True, null=True)
    cgpa = models.FloatField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
