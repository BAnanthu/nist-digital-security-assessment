from django.contrib.auth.models import User
from django.db import models

# Create your models here.
import category.models as category
import function.models as function
from report.data_model import MeturityScoringTABLE, ThreatScoringTABLE


class Assesmeent(models.Model):
    assessment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    identify = models.ForeignKey('function.Identify', on_delete=models.CASCADE, null=True, blank=True)
    protect = models.ForeignKey('function.Protect', on_delete=models.CASCADE, null=True, blank=True)
    detect = models.ForeignKey('function.Detect', on_delete=models.CASCADE, null=True, blank=True)
    respond = models.ForeignKey('function.Respond', on_delete=models.CASCADE, null=True, blank=True)
    recover = models.ForeignKey('function.Recover', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user_id.username


class IdentifyDataSet(models.Model):
    dataset_id = models.AutoField(primary_key=True)
    sub_category_id = models.ForeignKey('category.SubCategory', on_delete=models.CASCADE)
    process_level_value = models.ForeignKey(MeturityScoringTABLE, related_name="identify_process_level_value",
                                            on_delete=models.CASCADE)
    policy_level_value = models.ForeignKey(MeturityScoringTABLE, related_name="identify_policy_level_value",
                                           on_delete=models.CASCADE)
    Documentation_Level_value = models.ForeignKey(MeturityScoringTABLE,
                                                  related_name="identify_Documentation_Level_value",
                                                  on_delete=models.CASCADE)
    Automation_Level_value = models.ForeignKey(MeturityScoringTABLE, related_name="identify_Automation_Level_value",
                                               on_delete=models.CASCADE)
    Assessed_Maturity_Level_value = models.ForeignKey(ThreatScoringTABLE,
                                                      related_name="identify_Assessed_Maturity_Level_value",
                                                      on_delete=models.CASCADE,null=True)
    Primary_Threat_value = models.ForeignKey(ThreatScoringTABLE, related_name="identify_Primary_Threat_value",
                                             on_delete=models.CASCADE)
    Likelihood_of_Threat_value = models.ForeignKey(ThreatScoringTABLE,
                                                   related_name="identify_Likelihood_of_Threat_value",
                                                   on_delete=models.CASCADE)
    Impact_of_Threat_Occurrence_value = models.ForeignKey(ThreatScoringTABLE,
                                                          related_name="identify_Impact_of_Threat_Occurrence_value",
                                                          on_delete=models.CASCADE)
    ad_maturity_weight = models.IntegerField(null=True, blank=True)
    threat_weight = models.IntegerField(null=True, blank=True)
    likelihood_weight = models.IntegerField(null=True, blank=True)
    impact_weight = models.IntegerField(null=True, blank=True)
    severity = models.IntegerField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    identify_id = models.ForeignKey('function.Identify', on_delete=models.CASCADE, null=True, blank=True)
    category_id = models.ForeignKey('category.Category', on_delete=models.CASCADE, null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    desired_state = models.ForeignKey(ThreatScoringTABLE,
                                                      related_name="identify_desired_state",
                                                      on_delete=models.CASCADE,null=True)
    desired_state_severity = models.CharField(max_length=20,null=True, blank=True)

class ProtectDataSet(models.Model):
    dataset_id = models.AutoField(primary_key=True)
    sub_category_id = models.ForeignKey('category.SubCategory', on_delete=models.CASCADE)
    process_level_value = models.ForeignKey(MeturityScoringTABLE, related_name="protect_process_level_value",
                                            on_delete=models.CASCADE)
    policy_level_value = models.ForeignKey(MeturityScoringTABLE, related_name="protect_policy_level_value",
                                           on_delete=models.CASCADE)
    Documentation_Level_value = models.ForeignKey(MeturityScoringTABLE,
                                                  related_name="protect_Documentation_Level_value",
                                                  on_delete=models.CASCADE)
    Automation_Level_value = models.ForeignKey(MeturityScoringTABLE, related_name="protect_Automation_Level_value",
                                               on_delete=models.CASCADE)
    Assessed_Maturity_Level_value = models.ForeignKey(ThreatScoringTABLE,
                                                      related_name="protect_Assessed_Maturity_Level_value",
                                                      on_delete=models.CASCADE,null=True)
    Primary_Threat_value = models.ForeignKey(ThreatScoringTABLE, related_name="protect_Primary_Threat_value",
                                             on_delete=models.CASCADE)
    Likelihood_of_Threat_value = models.ForeignKey(ThreatScoringTABLE,
                                                   related_name="protect_Likelihood_of_Threat_value",
                                                   on_delete=models.CASCADE)
    Impact_of_Threat_Occurrence_value = models.ForeignKey(ThreatScoringTABLE,
                                                          related_name="protect_Impact_of_Threat_Occurrence_value",
                                                          on_delete=models.CASCADE)
    ad_maturity_weight = models.IntegerField(null=True, blank=True)
    threat_weight = models.IntegerField(null=True, blank=True)
    likelihood_weight = models.IntegerField(null=True, blank=True)
    impact_weight = models.IntegerField(null=True, blank=True)
    severity = models.IntegerField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    identify_id = models.ForeignKey('function.Protect', on_delete=models.CASCADE, null=True, blank=True)
    category_id = models.ForeignKey('category.Category', on_delete=models.CASCADE, null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    desired_state = models.ForeignKey(ThreatScoringTABLE,
                                      related_name="protect_desired_state",
                                      on_delete=models.CASCADE, null=True)
    desired_state_severity = models.CharField(max_length=20, null=True, blank=True)


class DetectDataSet(models.Model):
    dataset_id = models.AutoField(primary_key=True)
    sub_category_id = models.ForeignKey('category.SubCategory', on_delete=models.CASCADE)
    process_level_value = models.ForeignKey(MeturityScoringTABLE, related_name="detect_process_level_value",
                                            on_delete=models.CASCADE)
    policy_level_value = models.ForeignKey(MeturityScoringTABLE, related_name="detect_policy_level_value",
                                           on_delete=models.CASCADE)
    Documentation_Level_value = models.ForeignKey(MeturityScoringTABLE, related_name="detect_Documentation_Level_value",
                                                  on_delete=models.CASCADE)
    Automation_Level_value = models.ForeignKey(MeturityScoringTABLE, related_name="detect_Automation_Level_value",
                                               on_delete=models.CASCADE)
    Assessed_Maturity_Level_value = models.ForeignKey(ThreatScoringTABLE,
                                                      related_name="detect_Assessed_Maturity_Level_value",
                                                      on_delete=models.CASCADE,null=True)
    Primary_Threat_value = models.ForeignKey(ThreatScoringTABLE, related_name="detect_Primary_Threat_value",
                                             on_delete=models.CASCADE)
    Likelihood_of_Threat_value = models.ForeignKey(ThreatScoringTABLE, related_name="detect_Likelihood_of_Threat_value",
                                                   on_delete=models.CASCADE)
    Impact_of_Threat_Occurrence_value = models.ForeignKey(ThreatScoringTABLE,
                                                          related_name="detect_Impact_of_Threat_Occurrence_value",
                                                          on_delete=models.CASCADE)
    ad_maturity_weight = models.IntegerField(null=True, blank=True)
    threat_weight = models.IntegerField(null=True, blank=True)
    likelihood_weight = models.IntegerField(null=True, blank=True)
    impact_weight = models.IntegerField(null=True, blank=True)
    severity = models.IntegerField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    identify_id = models.ForeignKey('function.Detect', on_delete=models.CASCADE, null=True, blank=True)
    category_id = models.ForeignKey('category.Category', on_delete=models.CASCADE, null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    desired_state = models.ForeignKey(ThreatScoringTABLE,
                                      related_name="detect_desired_state",
                                      on_delete=models.CASCADE, null=True)
    desired_state_severity = models.CharField(max_length=20, null=True, blank=True)


class RespondDataSet(models.Model):
    dataset_id = models.AutoField(primary_key=True)
    sub_category_id = models.ForeignKey('category.SubCategory', on_delete=models.CASCADE)
    process_level_value = models.ForeignKey(MeturityScoringTABLE, related_name="respond_process_level_value",
                                            on_delete=models.CASCADE)
    policy_level_value = models.ForeignKey(MeturityScoringTABLE, related_name="respond_policy_level_value",
                                           on_delete=models.CASCADE)
    Documentation_Level_value = models.ForeignKey(MeturityScoringTABLE,
                                                  related_name="respond_Documentation_Level_value",
                                                  on_delete=models.CASCADE)
    Automation_Level_value = models.ForeignKey(MeturityScoringTABLE, related_name="respond_Automation_Level_value",
                                               on_delete=models.CASCADE)
    Assessed_Maturity_Level_value = models.ForeignKey(ThreatScoringTABLE,
                                                      related_name="respond_Assessed_Maturity_Level_value",
                                                      on_delete=models.CASCADE,null=True)
    Primary_Threat_value = models.ForeignKey(ThreatScoringTABLE, related_name="respond_Primary_Threat_value",
                                             on_delete=models.CASCADE)
    Likelihood_of_Threat_value = models.ForeignKey(ThreatScoringTABLE,
                                                   related_name="respond_Likelihood_of_Threat_value",
                                                   on_delete=models.CASCADE)
    Impact_of_Threat_Occurrence_value = models.ForeignKey(ThreatScoringTABLE,
                                                          related_name="respond_Impact_of_Threat_Occurrence_value",
                                                          on_delete=models.CASCADE)
    ad_maturity_weight = models.IntegerField(null=True, blank=True)
    threat_weight = models.IntegerField(null=True, blank=True)
    likelihood_weight = models.IntegerField(null=True, blank=True)
    impact_weight = models.IntegerField(null=True, blank=True)
    severity = models.IntegerField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    identify_id = models.ForeignKey('function.Respond', on_delete=models.CASCADE, null=True, blank=True)
    category_id = models.ForeignKey('category.Category', on_delete=models.CASCADE, null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    desired_state = models.ForeignKey(ThreatScoringTABLE,
                                      related_name="respond_desired_state",
                                      on_delete=models.CASCADE, null=True)
    desired_state_severity = models.CharField(max_length=20, null=True, blank=True)


class RecoverDataSet(models.Model):
    dataset_id = models.AutoField(primary_key=True)
    sub_category_id = models.ForeignKey('category.SubCategory', on_delete=models.CASCADE)
    process_level_value = models.ForeignKey(MeturityScoringTABLE, related_name="recover_process_level_value",
                                            on_delete=models.CASCADE)
    policy_level_value = models.ForeignKey(MeturityScoringTABLE, related_name="recover_policy_level_value",
                                           on_delete=models.CASCADE)
    Documentation_Level_value = models.ForeignKey(MeturityScoringTABLE,
                                                  related_name="recover_Documentation_Level_value",
                                                  on_delete=models.CASCADE)
    Automation_Level_value = models.ForeignKey(MeturityScoringTABLE, related_name="recover_Automation_Level_value",
                                               on_delete=models.CASCADE)
    Assessed_Maturity_Level_value = models.ForeignKey(ThreatScoringTABLE,
                                                      related_name="recover_Assessed_Maturity_Level_value",
                                                      on_delete=models.CASCADE,null=True)
    Primary_Threat_value = models.ForeignKey(ThreatScoringTABLE, related_name="recover_Primary_Threat_value",
                                             on_delete=models.CASCADE)
    Likelihood_of_Threat_value = models.ForeignKey(ThreatScoringTABLE,
                                                   related_name="recover_Likelihood_of_Threat_value",
                                                   on_delete=models.CASCADE)
    Impact_of_Threat_Occurrence_value = models.ForeignKey(ThreatScoringTABLE,
                                                          related_name="recover_Impact_of_Threat_Occurrence_value",
                                                          on_delete=models.CASCADE)
    ad_maturity_weight = models.IntegerField(null=True, blank=True)
    threat_weight = models.IntegerField(null=True, blank=True)
    likelihood_weight = models.IntegerField(null=True, blank=True)
    impact_weight = models.IntegerField(null=True, blank=True)
    severity = models.IntegerField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    identify_id = models.ForeignKey('function.Recover', on_delete=models.CASCADE, null=True, blank=True)
    category_id = models.ForeignKey('category.Category', on_delete=models.CASCADE, null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    desired_state = models.ForeignKey(ThreatScoringTABLE,
                                      related_name="recover_desired_state",
                                      on_delete=models.CASCADE, null=True)
    desired_state_severity = models.CharField(max_length=20, null=True, blank=True)


class FinalReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    severity_for_23_categories = models.TextField()
    calculated_priority_for_23_categories = models.TextField()
    entry_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

# Suggession Table
# category
# cs_maturity_level
# cs_threat_severity
# pa_maturity_level
# pa_threat_severity
# ds_maturity_level
# ds_threat_severity
# dataset_id
