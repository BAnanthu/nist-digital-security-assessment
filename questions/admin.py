from django.contrib import admin

# Register your models here.
from .models import Levels, Options
#
# admin.site.register(Levels)
# admin.site.register(Options)


@admin.register(Options)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("option_id", "level_id", "option")


@admin.register(Levels)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("level_id", "level_name", "level_details", "score_type")
