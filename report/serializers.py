from rest_framework import serializers, status
from rest_framework.serializers import Serializer

from report.models import IdentifyDataSet


class IdentifyDataSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentifyDataSet
        fields = ['sub_category_id', 'process_level_value',
                  'policy_level_value','Documentation_Level_value',
                  'Automation_Level_value',
                  'Primary_Threat_value','Likelihood_of_Threat_value',
                  'Impact_of_Threat_Occurrence_value','identify_id','category_id'
                  ]

    def create(self, validated_data):
        return IdentifyDataSet.objects.create(**validated_data)
