from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    url = models.TextField()
    pub_date = models.DateTimeField(default=timezone.datetime.now)
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def pub_date_pretty(self):
        return self.pub_date.strftime("%b %e %Y")

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
