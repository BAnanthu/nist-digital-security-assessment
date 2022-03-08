from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from function.models import IdentifyMaturityRoadMap
from report.calculations import assessedMaturityLevel, calcSeverity, calcLevel
from report.data_model import ThreatScoringTABLE
from report.models import IdentifyDataSet
from report.serializers import IdentifyDataSetSerializer


class CreateIdentifyDataSetView(APIView):

    def get_object(self, pk):
        return IdentifyDataSet.objects.get(pk=pk)

    def get(self, request):
        identify = IdentifyDataSet.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = IdentifyDataSetSerializer(identify, many=True)
        return Response({"data set": serializer.data})

    @staticmethod
    def post(request):
        identify_saved = None
        data = request.data

        print(data)

        # Create an article from the above data
        serializer = IdentifyDataSetSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            identify_saved = serializer.save()
            # identify_saved.Assessed_Maturity_Level_value = ThreatScoringTABLE.objects.get(id=2)
            identify_saved.save()
            print(identify_saved.process_level_value)
            """
            Finding Assessed-Maturity-Level_value
            # """
            process_level, policy_level, documentation_level, automation_level = [
                identify_saved.process_level_value.value, identify_saved.policy_level_value.value,
                identify_saved.Documentation_Level_value.value, identify_saved.Automation_Level_value.value
            ]
            assessedMaturityLevelList = assessedMaturityLevel(process_level, policy_level,
                                                              documentation_level, automation_level)
            identify_saved.Assessed_Maturity_Level_value = ThreatScoringTABLE.objects.get(
                id=assessedMaturityLevelList[1])

            identify_maturity_roadmap_instance = IdentifyMaturityRoadMap.objects.create(
                initial_risk=assessedMaturityLevelList[0][0],
                repeatable=assessedMaturityLevelList[0][1],
                defined=assessedMaturityLevelList[0][2],
                managed=assessedMaturityLevelList[0][3],
                optimizing=assessedMaturityLevelList[0][4],
                initial_risk_color=assessedMaturityLevelList[2][0],
                repeatable_color=assessedMaturityLevelList[2][1],
                defined_color=assessedMaturityLevelList[2][2],
                managed_color=assessedMaturityLevelList[2][3],
                optimizing_color=assessedMaturityLevelList[2][4],
                assessed_maturity_level=identify_saved.Assessed_Maturity_Level_value.option_id,
                identify_id=identify_saved.identify_id,
                dataset_id=IdentifyDataSet.objects.get(dataset_id=identify_saved.dataset_id),
            )
            """
            Finding ad_maturity_weight and SEVERITY
            SEVERITY = (Threat * Likelihood * Impact) / Adjusted Maturity				
            """
            primary_threat_value, likelihood_of_threat_value, impact_of_threat_occurrence_value = [
                identify_saved.Primary_Threat_value.value, identify_saved.Likelihood_of_Threat_value.value,
                identify_saved.Impact_of_Threat_Occurrence_value.value
            ]
            severity, ad_maturity_weight = calcSeverity(primary_threat_value,
                                                        likelihood_of_threat_value,
                                                        impact_of_threat_occurrence_value,
                                                        identify_saved.Assessed_Maturity_Level_value.value)
            identify_saved.severity = severity
            identify_saved.ad_maturity_weight = ad_maturity_weight

            """
            Finding threat_weight
            """
            identify_saved.threat_weight = primary_threat_value
            """
            Finding likelihood_weight
            """
            identify_saved.likelihood_weight = likelihood_of_threat_value
            """
            Finding impact_weight
            """
            identify_saved.impact_weight = impact_of_threat_occurrence_value
            """
            Finding level		
            """
            level, description = calcLevel(severity)
            identify_saved.level = level
            identify_saved.save()

        return Response({"success": "'{}' created successfully".format(identify_saved)})

    def patch(self, request, pk):
        identify_object = self.get_object(pk)
        serializer = IdentifyDataSetSerializer(identify_object, data=request.data,
                                               partial=True)  # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(code=201, data=serializer.data)
        return JsonResponse(code=400, data="wrong parameters")


