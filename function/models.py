from django.db import models

# Create your models here.
import category.models as category
# from report.models import RecoverDataSet, RespondDataSet, DetectDataSet, ProtectDataSet, IdentifyDataSet
from report.models import IdentifyDataSet, ProtectDataSet, RespondDataSet, RecoverDataSet, DetectDataSet


class Function(models.Model):
    function_id = models.AutoField(primary_key=True)
    function_index = models.IntegerField()
    function_name = models.CharField(max_length=70)
    function_details = models.TextField()

    def __str__(self):
        return self.function_name


class Identify(models.Model):
    id = models.AutoField(primary_key=True)
    identify_id = models.ForeignKey(Function, on_delete=models.CASCADE)
    category_id = models.ForeignKey('category.Category', related_name="identify", on_delete=models.CASCADE)
    MaturityScoreaverage = models.IntegerField(null=True, blank=True)
    MaturityRoadMapavg = models.IntegerField(null=True, blank=True)
    ThreatSeverityavg = models.IntegerField(null=True, blank=True)
    CalculatedPriorityavg = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id)


class IdentifyMaturityRoadMap(models.Model):
    COLOR = (
        ('W', 'White'),
        ('G', 'Gray'),
        ('O', 'Orange'),
    )

    ASSESSED_MATURITY_LEVEL = (('Select A Response', 'Select A Response'),
                               ('Non-Existent', 'Non-Existent'),
                               ('Initial', 'Initial'),
                               ('Developing', 'Developing'),
                               ('Defined', 'Defined'),
                               ('Managed', 'Managed'),
                               ('Optimized', 'Optimized')
                               )

    map_id = models.AutoField(primary_key=True)
    # user_id
    initial_risk = models.IntegerField()
    repeatable = models.IntegerField()
    defined = models.IntegerField()
    managed = models.IntegerField()
    optimizing = models.IntegerField()
    initial_risk_color = models.CharField(choices=COLOR, default=None, null=True, max_length=1)
    repeatable_color = models.CharField(choices=COLOR, default=None, null=True, max_length=1)
    defined_color = models.CharField(choices=COLOR, default=None, null=True, max_length=1)
    managed_color = models.CharField(choices=COLOR, default=None, null=True, max_length=1)
    optimizing_color = models.CharField(choices=COLOR, default=None, null=True, max_length=1)
    assessed_maturity_level = models.CharField(choices=ASSESSED_MATURITY_LEVEL, default=None, max_length=20)
    assessed_maturity_level_value = models.IntegerField(default=0, null=True)
    # assessment_id
    dataset_id = models.ForeignKey(IdentifyDataSet, on_delete=models.CASCADE)
    # category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    identify_id = models.ForeignKey(Identify, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.identify_id)


"""
    PROTECT
"""


class Protect(models.Model):
    id = models.AutoField(primary_key=True)
    protect_id = models.ForeignKey(Function, on_delete=models.CASCADE)
    category_id = models.ForeignKey('category.Category', related_name="protect", on_delete=models.CASCADE, null=True)
    MaturityScoreaverage = models.IntegerField(null=True, blank=True)
    MaturityRoadMapavg = models.IntegerField(null=True, blank=True)
    ThreatSeverityavg = models.IntegerField(null=True, blank=True)
    CalculatedPriorityavg = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id)


class ProtectMaturityRoadMap(models.Model):
    COLOR = (
        ('W', 'White'),
        ('G', 'Gray'),
        ('O', 'Orange'),
    )

    ASSESSED_MATURITY_LEVEL = (('SAR', 'Select A Response'),
                               ('NE', 'Non - Existent'),
                               ('I', 'Initial'),
                               ('DEV', 'Developing'),
                               ('DEF', 'Defined'),
                               ('M', 'Managed'),
                               ('O', 'Optimized')
                               )

    map_id = models.AutoField(primary_key=True)
    # user_id
    initial_risk = models.IntegerField()
    repeatable = models.IntegerField()
    defined = models.IntegerField()
    managed = models.IntegerField()
    optimizing = models.IntegerField()
    initial_risk_color = models.CharField(choices=COLOR, default=None, null=True, max_length=1)
    repeatable_color = models.CharField(choices=COLOR, default=None, null=True, max_length=1)
    defined_color = models.CharField(choices=COLOR, default=None, null=True, max_length=1)
    managed_color = models.CharField(choices=COLOR, default=None, null=True, max_length=1)
    optimizing_color = models.CharField(choices=COLOR, default=None, null=True, max_length=1)
    assessed_maturity_level = models.CharField(choices=ASSESSED_MATURITY_LEVEL, default=None, max_length=3)
    assessed_maturity_level_value = models.IntegerField(default=0, null=True)
    # assessment_id
    dataset_id = models.ForeignKey(ProtectDataSet, on_delete=models.CASCADE)
    # category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    identify_id = models.ForeignKey(Protect, on_delete=models.CASCADE)


"""
    DETECT
"""


class Detect(models.Model):
    id = models.AutoField(primary_key=True)
    detect_id = models.ForeignKey(Function, on_delete=models.CASCADE)
    category_id = models.ForeignKey('category.Category', related_name="detect", on_delete=models.CASCADE, null=True)
    MaturityScoreaverage = models.IntegerField(null=True, blank=True)
    MaturityRoadMapavg = models.IntegerField(null=True, blank=True)
    ThreatSeverityavg = models.IntegerField(null=True, blank=True)
    CalculatedPriorityavg = models.IntegerField(null=True, blank=True)


class DetectMaturityRoadMap(models.Model):
    COLOR = (
        ('W', 'White'),
        ('G', 'Gray'),
        ('O', 'Orange'),
    )

    ASSESSED_MATURITY_LEVEL = (('SAR', 'Select A Response'),
                               ('NE', 'Non - Existent'),
                               ('I', 'Initial'),
                               ('DEV', 'Developing'),
                               ('DEF', 'Defined'),
                               ('M', 'Managed'),
                               ('O', 'Optimized')
                               )

    map_id = models.AutoField(primary_key=True)
    # user_id
    initial_risk = models.IntegerField()
    repeatable = models.IntegerField()
    defined = models.IntegerField()
    managed = models.IntegerField()
    optimizing = models.IntegerField()
    initial_risk_color = models.CharField(choices=COLOR, default=None, null=True, max_length=1)
    repeatable_color = models.CharField(choices=COLOR, default=None, null=True, max_length=1)
    defined_color = models.CharField(choices=COLOR, default=None, null=True, max_length=1)
    managed_color = models.CharField(choices=COLOR, default=None, null=True, max_length=1)
    optimizing_color = models.CharField(choices=COLOR, default=None, null=True, max_length=1)
    assessed_maturity_level = models.CharField(choices=ASSESSED_MATURITY_LEVEL, default=None, max_length=3)
    assessed_maturity_level_value = models.IntegerField(default=0, null=True)
    # assessment_id
    dataset_id = models.ForeignKey(DetectDataSet, on_delete=models.CASCADE)
    # category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    identify_id = models.ForeignKey(Detect, on_delete=models.CASCADE)


"""
    RESPOND
"""


class Respond(models.Model):
    id = models.AutoField(primary_key=True)
    respond_id = models.ForeignKey(Function, on_delete=models.CASCADE)
    category_id = models.ForeignKey('category.Category', related_name="respond", on_delete=models.CASCADE, null=True)
    MaturityScoreaverage = models.IntegerField(null=True, blank=True)
    MaturityRoadMapavg = models.IntegerField(null=True, blank=True)
    ThreatSeverityavg = models.IntegerField(null=True, blank=True)
    CalculatedPriorityavg = models.IntegerField(null=True, blank=True)


class RespondMaturityRoadMap(models.Model):
    COLOR = (
        ('W', 'White'),
        ('G', 'Gray'),
        ('O', 'Orange'),
    )

    ASSESSED_MATURITY_LEVEL = (('SAR', 'Select A Response'),
                               ('NE', 'Non - Existent'),
                               ('I', 'Initial'),
                               ('DEV', 'Developing'),
                               ('DEF', 'Defined'),
                               ('M', 'Managed'),
                               ('O', 'Optimized')
                               )

    map_id = models.AutoField(primary_key=True)
    # user_id
    initial_risk = models.IntegerField()
    repeatable = models.IntegerField()
    defined = models.IntegerField()
    managed = models.IntegerField()
    optimizing = models.IntegerField()
    initial_risk_color = models.CharField(choices=COLOR, default=None, null=True, max_length=1)
    repeatable_color = models.CharField(choices=COLOR, default=None, null=True, max_length=1)
    defined_color = models.CharField(choices=COLOR, default=None, null=True, max_length=1)
    managed_color = models.CharField(choices=COLOR, default=None, null=True, max_length=1)
    optimizing_color = models.CharField(choices=COLOR, default=None, null=True, max_length=1)
    assessed_maturity_level = models.CharField(choices=ASSESSED_MATURITY_LEVEL, default=None, max_length=3)
    assessed_maturity_level_value = models.IntegerField(default=0, null=True)
    # assessment_id
    dataset_id = models.ForeignKey(RespondDataSet, on_delete=models.CASCADE)
    # category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    identify_id = models.ForeignKey(Respond, on_delete=models.CASCADE)


"""
    RECOVER
"""


class Recover(models.Model):
    id = models.AutoField(primary_key=True)
    recover_id = models.ForeignKey(Function, on_delete=models.CASCADE)
    category_id = models.ForeignKey('category.Category', related_name="recover", on_delete=models.CASCADE, null=True)
    MaturityScoreaverage = models.IntegerField(null=True, blank=True)
    MaturityRoadMapavg = models.IntegerField(null=True, blank=True)
    ThreatSeverityavg = models.IntegerField(null=True, blank=True)
    CalculatedPriorityavg = models.IntegerField(null=True, blank=True)


class RecoverMaturityRoadMap(models.Model):
    COLOR = (
        ('W', 'White'),
        ('G', 'Gray'),
        ('O', 'Orange'),
    )

    ASSESSED_MATURITY_LEVEL = (('SAR', 'Select A Response'),
                               ('NE', 'Non - Existent'),
                               ('I', 'Initial'),
                               ('DEV', 'Developing'),
                               ('DEF', 'Defined'),
                               ('M', 'Managed'),
                               ('O', 'Optimized')
                               )

    map_id = models.AutoField(primary_key=True)
    # user_id
    initial_risk = models.IntegerField()
    repeatable = models.IntegerField()
    defined = models.IntegerField()
    managed = models.IntegerField()
    optimizing = models.IntegerField()
    initial_risk_color = models.CharField(choices=COLOR, default=None, null=True, max_length=1)
    repeatable_color = models.CharField(choices=COLOR, default=None, null=True, max_length=1)
    defined_color = models.CharField(choices=COLOR, default=None, null=True, max_length=1)
    managed_color = models.CharField(choices=COLOR, default=None, null=True, max_length=1)
    optimizing_color = models.CharField(choices=COLOR, default=None, null=True, max_length=1)
    assessed_maturity_level = models.CharField(choices=ASSESSED_MATURITY_LEVEL, default=None, max_length=3)
    assessed_maturity_level_value = models.IntegerField(default=0, null=True)
    # assessment_id
    dataset_id = models.ForeignKey(RecoverDataSet, on_delete=models.CASCADE)
    # category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    identify_id = models.ForeignKey(Recover, on_delete=models.CASCADE)
