from django.db import models

# Create your models here.


class Interview(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    questions = models.JSONField() #We must write questions in JSON format(enclosed in a List or square brackets)
    date_interviewed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title