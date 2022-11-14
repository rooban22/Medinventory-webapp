from cgi import print_exception
from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Medicine(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=200,)
    price =models.IntegerField(default=0) 
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500,default=0)
    image = models.ImageField(blank = True,upload_to = 'images')