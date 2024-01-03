from django.db import models

# Create your models here.
class HistoryList (models.Model):
    date = models.CharField(max_length=300)
    text = models.CharField(max_length=300)

