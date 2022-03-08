from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from function.models import Identify
from function.serializers import IdentifySerializer
from report.calculations import calcIdentifyAverageByCategory


class CreateIdentifyByCategoryView(APIView):

    def get_object(self, pk):
        return Identify.objects.get(pk=pk)

    def get(self, request):
        identify = Identify.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = IdentifySerializer(identify, many=True)
        return Response({"identify": serializer.data})

    @staticmethod
    def post(request):
        identify_saved = None
        data = request.data

        # Create an article from the above data
        serializer = IdentifySerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            identify_saved = serializer.save()
        return Response({"success": "Identify By Category '{}' created successfully".format(identify_saved)})

    def patch(self, request, pk):
        identify_object = self.get_object(pk)

        MaturityScoreaverage, MaturityRoadMapavg, ThreatSeverityavg = calcIdentifyAverageByCategory(request.data['identify_id'],
                                                                                                    request.data['category_id'])

        serializer = IdentifySerializer(identify_object, data=request.data,
                                        partial=True)  # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save(MaturityScoreaverage=MaturityScoreaverage,
                            MaturityRoadMapavg=MaturityRoadMapavg,
                            ThreatSeverityavg=ThreatSeverityavg
                            )
            return Response({"success": "updated successfully"})
        return JsonResponse(code=400, data="wrong parameters")
