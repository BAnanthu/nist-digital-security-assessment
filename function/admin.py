from django.contrib import admin

# Register your models here.
from .models import Function,Identify,IdentifyMaturityRoadMap,\
    Protect,ProtectMaturityRoadMap,Detect,\
    DetectMaturityRoadMap,Respond,RespondMaturityRoadMap,\
    Recover,RecoverMaturityRoadMap

# Register your models here.
# admin.site.register(Function)
# admin.site.register(Identify)
# admin.site.register(IdentifyMaturityRoadMap)
# admin.site.register(Protect)

admin.site.register(ProtectMaturityRoadMap)
admin.site.register(Detect)
admin.site.register(DetectMaturityRoadMap)
admin.site.register(Respond)
admin.site.register(RespondMaturityRoadMap)
admin.site.register(Recover)
admin.site.register(RecoverMaturityRoadMap)


@admin.register(Function)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("function_id", "function_index","function_name","function_details")

@admin.register(Identify)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("identify_id", "MaturityScoreaverage","MaturityRoadMapavg","ThreatSeverityavg","CalculatedPriorityavg")


@admin.register(IdentifyMaturityRoadMap)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("map_id", "initial_risk","repeatable","defined","managed","optimizing","assessed_maturity_level","dataset_id","identify_id")

@admin.register(Protect)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("protect_id", "MaturityScoreaverage","MaturityRoadMapavg","ThreatSeverityavg","CalculatedPriorityavg")