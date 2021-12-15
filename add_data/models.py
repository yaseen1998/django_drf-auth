from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
# Create your models here.

class Add_data(models.Model):
    anime_name = models.CharField(max_length=64)
    anime_desc = models.TextField()
    anime_rank = models.IntegerField()
    anime_watcher = models.ForeignKey(get_user_model(),on_delete=CASCADE)
    anime_country = models.CharField(max_length=64)
    anime_type = models.CharField(max_length=64)
    created_at = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = False, auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.anime_name