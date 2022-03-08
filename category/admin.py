from django.contrib import admin
from .models import Category, SubCategory

# Register your models here.
# admin.site.register(Category)
# admin.site.register(SubCategory)


@admin.register(Category)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("category_id", "category_index", "function_id", "category_name", "category_tag", "category_details")


@admin.register(SubCategory)
class PersonAdmin(admin.ModelAdmin):
    # list_display = ("subcategory_id", "subcategory_index", "category_id", "function_id", "subcategory_name", "subcategory_details")
    list_display = ("subcategory_index", "category_id", "function_id", "subcategory_name", "subcategory_details")
