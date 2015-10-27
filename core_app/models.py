from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
	user = models.ForeignKey(User,related_name='item')
	item_id = models.CharField(max_length=30)
	count = models.IntegerField(default=0)