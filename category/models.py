from django.db import models


# Create your models here.
from function.models import Function


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_index = models.IntegerField()
    function_id = models.ForeignKey(Function,related_name="category", on_delete=models.CASCADE)
    category_name = models.CharField(max_length=70)
    category_tag = models.CharField(max_length=20)
    category_details = models.TextField()

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    subcategory_id = models.AutoField(primary_key=True)
    subcategory_index = models.IntegerField()
    category_id = models.ForeignKey(Category,related_name="subcategory", on_delete=models.CASCADE)
    function_id = models.ForeignKey(Function,related_name="subcategory", on_delete=models.CASCADE,null=True)
    subcategory_name = models.CharField(max_length=70)
    subcategory_details = models.TextField()

    def __str__(self):
        return self.subcategory_name