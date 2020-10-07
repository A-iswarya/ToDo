from django.db import models

#a model with 2 fields 
class ToDo(models.Model):
    text = models.CharField(max_length = 45);
    completed = models.BooleanField(default = False);
    def __str__(self):
        return self.text;
