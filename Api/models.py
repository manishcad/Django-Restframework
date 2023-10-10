from django.db import models

# Create your models here.

class Register_Model(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    image=models.FileField(upload_to="Files")

    def __str__(self):
        return self.username
    
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(Register_Model,on_delete=models.CASCADE)

    def __str__(self):
        return self.title