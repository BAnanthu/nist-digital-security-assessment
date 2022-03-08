from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Userdetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=20, default=None, null=True)
    gender = models.CharField(max_length=6, default=None)
    contact = models.CharField(max_length=10, default=None, null=True)
    date_of_birth = models.DateField(default=None)
    location = models.CharField(max_length=50, default=None, null=True)
    city = models.CharField(max_length=20, default=None, null=True)
    state = models.CharField(max_length=20, default=None, null=True)
    country = models.CharField(max_length=20, default=None, null=True)

    # profile_pic = models.FileField(upload_to="profile-pic",default=None,null=True)

    class Meta:
        verbose_name_plural = "User Details"

    def __str__(self):
        return self.user.username


# class UserProgress(models.Model):
#     progress_id = models.AutoField(primary_key=True)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE())
