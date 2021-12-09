from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Blog(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tittle=models.CharField(max_length=50)
    Img = models.ImageField(upload_to='images/',blank=True,null=True)
    dsc = models.TextField(max_length=1500)
    date = models.DateTimeField(auto_now_add=True)
    pname = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.tittle