from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    info = models.TextField(blank=True, null=True)
    related_tags = models.ManyToManyField('self', blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse_lazy('tag_detail', args=[self.pk])

    def __str__(self):
        return self.name
