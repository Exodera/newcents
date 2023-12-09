from django.db import models

class App(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, default="Application description")
    date_added = models.DateTimeField()
    link = models.CharField(max_length=100, default="/link")
    
    
    def __str__(self):
        return self.name
