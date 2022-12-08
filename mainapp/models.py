from django.db import models

class Yangilik(models.Model):
    rasm=models.FileField()
    sarlavha=models.CharField(max_length=100)
    sana=models.DateField()
    matn=models.TextField()
    korish_soni=models.PositiveSmallIntegerField(default=0)


