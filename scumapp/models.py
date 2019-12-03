from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='items/')
    size = models.CharField(max_length=50)
    price1 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=100)
    button_ym = models.CharField(max_length=250)

    def _str_(self):
        return '{}'.format(self.name)


class Review(models.Model):
    user = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    userpic = models.ImageField(upload_to='userpics/')
    reviewpic = models.ImageField(upload_to='reviewpics/')
    likes = models.CharField(max_length=30)
    review = models.TextField(max_length=10000)
    date = models.CharField(max_length=10)

    def _str_(self):
        return '{}'.format(self.user)
