from django.db import models

class HistoryList (models.Model):
    date = models.CharField(max_length=300)
    text = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.pk} {self.text}'

class MainContent (models.Model):
    type = models.CharField(max_length=300)
    text = models.TextField()
    history_list = models.ForeignKey(HistoryList, on_delete=models.SET_NULL, null=True)

class Subtopics (models.Model):
    title = models.CharField(max_length=300)
    history_list = models.ForeignKey(HistoryList, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'ID: {self.pk}  Title: {self.title}  HL:{self.history_list}'

class SubtopicsContent (models.Model):
    type = models.CharField(max_length=300,blank=True)
    text = models.TextField()
    subtopics = models.ForeignKey(Subtopics, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.pk} {self.text} {self.subtopics}'






