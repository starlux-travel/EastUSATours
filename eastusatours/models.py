# eastusatours/models.py
from django.db import models

class Tour(models.Model):
    title_zh_tw = models.CharField(max_length=255)
    title_zh_cn = models.CharField(max_length=255, blank=True)
    title_en = models.CharField(max_length=255, blank=True)

    description_zh_tw = models.TextField(blank=True)
    description_zh_cn = models.TextField(blank=True)
    description_en = models.TextField(blank=True)

    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title_zh_tw
