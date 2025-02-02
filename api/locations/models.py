from django.db import models
from django.utils.text import slugify

# Create your models here.
class StudyArea(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, primary_key=True, editable=False)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """genarates slug from name"""
        self.slug = slugify(self.name)
        super(StudyArea, self).save(*args, **kwargs)