from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Progress(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    identify = models.TextField()
    protect = models.TextField()
    detect = models.TextField()
    recover = models.TextField()
    respond = models.TextField()
    category_attended = models.TextField()



