from django.db.models import Avg
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import SubCategorySerializer, FunctionSerializer
from category.models import SubCategory
from category.models import Category
from function.models import Identify, Function
from report.calculations import assessedMaturityLevel, calcSeverity, calcLevel
from report.data_model import MeturityScoringTABLE, ThreatScoringTABLE
from report.models import IdentifyDataSet, ProtectDataSet, RecoverDataSet, RespondDataSet, DetectDataSet


class GetData(APIView):
    def get(self, request):
        queryset = SubCategory.objects.order_by('subcategory_index')
        total_questions = len(queryset)
        current_question_index = 0
        serializer = SubCategorySerializer(queryset, many=True)

        data = list(serializer.data)

        questions_list = []
        for question in data:
            # print(question, end="\n\n")
            questions_list.append(question)
            questions_list.append({"Type": "report",
                                   "function_id": str(question["function_id"]),
                                   "function_name": str(question["function_name"]),
                                   "category_id": str(question["category_id"]),
                                   "category_name": str(question["category_name"]),
                                   "subcategory_id": str(question["subcategory_id"]),
                                   "subcategory_index": str(question["subcategory_index"]),
                                   "subcategory_name": str(question["subcategory_name"]),
                                   "subcategory_details": str(question["subcategory_details"]),
                                   "Maturity-Level": {"Your-Current-State": "",
                                                      "Peer-Average": "",
                                                      "Your-Desired-State": "",
                                                      },
                                   "Threat-Severity": {"Your-Current-State": "",
                                                       "Peer-Average": "",
                                                       "Your-Desired-State": "",
                                                       }
                                   })

            """
            report by category
            """

        # def build_dict(seq, key):
        #     return dict((d[key], dict(d, index=index)) for (index, d) in enumerate(seq))
        # category_obj = Category.objects.all().order_by('category_index').distinct()
        # for category in tuple(category_obj):
        #     people_by_name = build_dict(data, key="category_id")
        #     tom_info = people_by_name.get(category.category_id)
        #     print(tom_info["index"])
        #     data.insert(tom_info["index"]+1,{"Type":"report",
        #                    "function_id":str(category.function_id.function_id),
        #                    "function_name": str(category.function_id.function_name),
        #                    "category_id":str(category.category_id),
        #                    "category_name": str(category.category_name),
        #                    "Maturity-Level":{"Your-Current-State":"",
        #                                      "Peer-Average": "",
        #                                      "Your-Desired-State": "",
        #                                      },
        #                    "Threat-Severity": {"Your-Current-State": "",
        #                                       "Peer-Average": "",
        #                                       "Your-Desired-State": "",
        #                                       }
        #                    })
        return Response({
            "total_questions": total_questions,
            "total_questions": current_question_index,
            "questions": questions_list
        })


class Progress(APIView):
    pass


class FunctionView(APIView):

    def get(self, request):
        queryset = Function.objects.order_by('function_index')
        serializer = FunctionSerializer(queryset, many=True)

        return Response({
            "functions": serializer.data
        })




class AssessedMaturityLevelView(APIView):

    def post(self, request):
        process_level = MeturityScoringTABLE.objects.get(
            option_id__option_id=int(request.POST.get("process-level")))
        policy_level = MeturityScoringTABLE.objects.get(
            option_id__option_id=int(request.POST.get("policy-level")))
        documentation_level = MeturityScoringTABLE.objects.get(
            option_id__option_id=int(request.POST.get("documentation-level")))
        automation_level = MeturityScoringTABLE.objects.get(
            option_id__option_id=int(request.POST.get("automation-level")))
        print(process_level.value, policy_level.value, documentation_level.value, automation_level.value)
        assessedMaturityList = assessedMaturityLevel(process_level.value, policy_level.value, documentation_level.value,
                                                     automation_level.value)
        assessedMaturitID = assessedMaturityList[1]
        maturityOptionId = ThreatScoringTABLE.objects.get(id=assessedMaturitID)

        return Response({
            "option_id": maturityOptionId.option_id.option_id,
            "level_id": maturityOptionId.level_id.level_id,
        })


class YourDesiredLevelView(APIView):

    def get(self, request):
        print(request)
        print(dir(request))
        report_id = request.query_params.get("report_id")
        function_id = request.query_params.get("function_id")
        print("report_id", report_id)
        assessed_maturity_level_id = int(request.query_params.get("desired_state"))

        assessed_maturity_level = ThreatScoringTABLE.objects.get(id=assessed_maturity_level_id)
        assessed_maturity_level_value = assessed_maturity_level.value

        print("report_id", "assessed_maturity_level_value", report_id, assessed_maturity_level_value)
        print(function_id)
        function = Function.objects.get(function_id=function_id)
        if function.function_name == 'IDENTIFY':
            report = IdentifyDataSet.objects.get(dataset_id=report_id)
        elif function.function_name == 'PROTECT':
            report = ProtectDataSet.objects.get(dataset_id=report_id)
        elif function.function_name == 'DETECT':
            report = DetectDataSet.objects.get(dataset_id=report_id)
        elif function.function_name == 'RESPOND':
            report = RespondDataSet.objects.get(dataset_id=report_id)
        elif function.function_name == 'RECOVER':
            report = RecoverDataSet.objects.get(dataset_id=report_id)

        print("report_id:", report)
        primary_threat_value = report.threat_weight
        likelihood_of_threat_value = report.likelihood_weight
        impact_of_threat_occurrence_value = report.impact_weight

        severity, assessed_maturity_level_value = calcSeverity(primary_threat_value, likelihood_of_threat_value,
                                                               impact_of_threat_occurrence_value,
                                                               assessed_maturity_level_value)
        level, description = calcLevel(severity)
        report.desired_state = assessed_maturity_level
        report.desired_state_severity = description
        report.save()
        return Response({
            "threat_severity": description,
        })
