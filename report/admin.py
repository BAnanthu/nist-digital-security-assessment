from django.contrib import admin

# Register your models here.
from .models import Assesmeent, IdentifyDataSet, ProtectDataSet, \
    DetectDataSet, RespondDataSet, RecoverDataSet, FinalReport

from .data_model import MeturityScoringTABLE, ThreatScoringTABLE

# admin.site.register(Assesmeent)
# admin.site.register(IdentifyDataSet)
admin.site.register(ProtectDataSet)
admin.site.register(DetectDataSet)
admin.site.register(RespondDataSet)
admin.site.register(RecoverDataSet)
admin.site.register(FinalReport)


#
# admin.site.register(MeturityScoringTABLE)
# admin.site.register(ThreatScoringTABLE)

@admin.register(IdentifyDataSet)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("dataset_id", "sub_category_id", "process_level_value", "policy_level_value",
                    "Documentation_Level_value","Automation_Level_value","Assessed_Maturity_Level_value",
                    "Primary_Threat_value","Likelihood_of_Threat_value","Impact_of_Threat_Occurrence_value",
                    "ad_maturity_weight","threat_weight","likelihood_weight","impact_weight","severity","level",
                    "identify_id","category_id","total"
                    )


@admin.register(Assesmeent)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("assessment_id", "user_id", "identify", "protect", "detect", "respond", "recover")


@admin.register(MeturityScoringTABLE)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("id", "level_id", "option_id", "value")


@admin.register(ThreatScoringTABLE)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("id", "level_id", "option_id", "value")
