from django.db import models

# Create your models here.

class Promt(models.Model):
    prompt_text=models.CharField(max_length=1000)
