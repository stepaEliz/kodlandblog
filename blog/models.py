from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255, null=True)
    content = models.CharField(max_length=400, null=True)
    image = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title