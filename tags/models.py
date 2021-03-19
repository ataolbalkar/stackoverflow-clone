from django.db import models


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    info = models.TextField(blank=True, null=True)
    related_tags = models.ManyToManyField('self', blank=True)

    def get_absolute_url(self):
        return f'/{self.pk}'

    def __str__(self):
        return self.name
