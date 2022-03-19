from django.db.models import Avg
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.shortcuts import get_object_or_404
# find user assesment id
from function.models import Identify, Function, IdentifyMaturityRoadMap, Protect, Detect, Respond, Recover, \
    ProtectMaturityRoadMap, DetectMaturityRoadMap, RespondMaturityRoadMap, RecoverMaturityRoadMap
from category.models import Category, SubCategory
from questions.models import Options, Levels
from report.calculations import assessedMaturityLevel, calcSeverity, calcLevel
from report.data_model import MeturityScoringTABLE, ThreatScoringTABLE
from report.models import Assesmeent, IdentifyDataSet, ProtectDataSet, DetectDataSet, RespondDataSet, RecoverDataSet


def getYourDesiredState():
    return ThreatScoringTABLE.objects.filter(level_id__level_name="Assessed Maturity Level")


def findUserAssesmentID(user):
    return Assesmeent.objects.get(user_id=user)


def PeerAverage(sub_category_id, function_id):
    asd_maturity_level_id = None
    severity = None
    if function_id.function_name == 'IDENTIFY':
        asmaturity_level_avg = IdentifyDataSet.objects.filter(sub_category_id=sub_category_id.subcategory_id).aggregate(
            Avg('Assessed_Maturity_Level_value__value'), Avg('level'))
    elif function_id.function_name == 'PROTECT':
        asmaturity_level_avg = ProtectDataSet.objects.filter(sub_category_id=sub_category_id.subcategory_id).aggregate(
            Avg('Assessed_Maturity_Level_value__value'), Avg('level'))
    elif function_id.function_name == 'DETECT':
        asmaturity_level_avg = DetectDataSet.objects.filter(sub_category_id=sub_category_id.subcategory_id).aggregate(
            Avg('Assessed_Maturity_Level_value__value'), Avg('level'))
    elif function_id.function_name == 'RESPOND':
        asmaturity_level_avg = RespondDataSet.objects.filter(sub_category_id=sub_category_id.subcategory_id).aggregate(
            Avg('Assessed_Maturity_Level_value__value'), Avg('level'))
    elif function_id.function_name == 'RECOVER':
        asmaturity_level_avg = RecoverDataSet.objects.filter(sub_category_id=sub_category_id.subcategory_id).aggregate(
            Avg('Assessed_Maturity_Level_value__value'), Avg('level'))
    asd_maturity_avg = asmaturity_level_avg['Assessed_Maturity_Level_value__value__avg']
    level_avg = asmaturity_level_avg['level__avg']
    print(asmaturity_level_avg)

    # finding average maturity level id
    if asd_maturity_avg < 10:
        asd_maturity_level_id = 2
    elif 10 <= asd_maturity_avg < 20:
        asd_maturity_level_id = 3
    elif 20 <= asd_maturity_avg < 50:
        asd_maturity_level_id = 4
    elif 50 <= asd_maturity_avg < 80:
        asd_maturity_level_id = 5
    elif 80 <= asd_maturity_avg < 90:
        asd_maturity_level_id = 6
    elif asd_maturity_avg >= 90:
        asd_maturity_level_id = 7

    # finding average level by fro rages
    if level_avg < 2:
        severity = 'Low'
    elif 2 <= level_avg < 3:
        severity = 'Medium'
    elif 3 <= level_avg < 4:
        severity = 'High'
    elif level_avg >= 4:
        severity = 'Critical'

    return asd_maturity_level_id, severity


"find function id's of user"


def findFunctionID(assesment):
    function_ids = {
        'identify': assesment.identify,
        'protect': assesment.protect,
        'detect': assesment.detect,
        'respond': assesment.respond,
        'recover': assesment.recover
    }
    return function_ids


def getOptions():
    context = {}
    context['levels'] = []
    levels = Levels.objects.order_by('level_id')
    print(levels)
    for level in levels:
        context['levels'].append(level)
    # for lev in levels:
    # context[(lev.level_name).replace(' ','_')] = [op for op in MeturityScoringTABLE.objects.filter(level_id=lev.level_id).order_by('id')]
    context['options'] = [op for op in MeturityScoringTABLE.objects.all()] + [op for op in
                                                                              ThreatScoringTABLE.objects.all()]

    # print(context)
    return context


def getFistQuestion(function_id, category_id, sub_category_id, assesment, direction):
    print(type(sub_category_id), sub_category_id)
    print("sub_category_id.subcategory_id", sub_category_id.subcategory_id, function_id.function_id, )
    category = category_id.category_id
    function = function_id.function_id
    if not SubCategory.objects.filter(subcategory_id=sub_category_id.subcategory_id,
                                      function_id=function_id.function_id,
                                      category_id=category_id.category_id).exists():
        if direction == "next":
            category = category_id.category_id + 1
        elif direction == "previous":
            category = category_id.category_id - 1
        if not SubCategory.objects.filter(subcategory_id=sub_category_id.subcategory_id,
                                          function_id=function_id.function_id,
                                          category_id=category).exists():
            if direction == "next":
                function = function_id.function_id + 1
                # set function id to assessment table if not exist
                function_id_dict = findFunctionID(assesment)
                if not function_id_dict['identify'] and function == 1:
                    identify_obj = Identify()
                    identify_obj.identify_id = function_id
                    identify_obj.category_id = category_id
                    identify_obj.save()
                    assesment.identify = identify_obj
                    assesment.save()
                elif not function_id_dict['protect'] and function == 2:
                    protect_obj = Protect()
                    protect_obj.protect_id = function_id
                    protect_obj.category_id = category_id
                    protect_obj.save()
                    assesment.protect = protect_obj
                    assesment.save()
                elif not function_id_dict['detect'] and function == 3:
                    detect_obj = Detect()
                    detect_obj.detect_id = function_id
                    detect_obj.category_id = category_id
                    detect_obj.save()
                    assesment.detect = detect_obj
                    assesment.save()
                elif not function_id_dict['respond'] and function == 4:
                    respond_obj = Respond()
                    respond_obj.respond_id = function_id
                    respond_obj.category_id = category_id
                    respond_obj.save()
                    assesment.respond = respond_obj
                    assesment.save()
                elif not function_id_dict['recover'] and function == 5:
                    recover_obj = Recover()
                    recover_obj.recover_id = function_id
                    recover_obj.category_id = category_id
                    recover_obj.save()
                    assesment.recover = recover_obj
                    assesment.save()
                else:
                    pass
            elif direction == "previous":
                function = function_id.function_id - 1

    # print(function_id.function_id, category_id.category_id, sub_category_id.subcategory_id)
    print(function, category, sub_category_id.subcategory_id)
    subcategory = get_object_or_404(SubCategory, function_id=function,
                                    category_id=category,
                                    subcategory_id=sub_category_id.subcategory_id)
    answers = None
    print(" function_id.function_name8//", function_id.function_name)
    if function == 1 and IdentifyDataSet.objects.filter(identify_id=assesment.identify,
                                                        sub_category_id=sub_category_id,
                                                        category_id=category).exists():
        answers = IdentifyDataSet.objects.get(identify_id=assesment.identify,
                                              sub_category_id=sub_category_id,
                                              category_id=category)
    elif function == 2 and ProtectDataSet.objects.filter(identify_id=assesment.protect,
                                                         sub_category_id=sub_category_id,
                                                         category_id=category).exists():
        answers = ProtectDataSet.objects.get(identify_id=assesment.protect,
                                             sub_category_id=sub_category_id,
                                             category_id=category)
    elif function == 3 and DetectDataSet.objects.filter(identify_id=assesment.detect,
                                                        sub_category_id=sub_category_id,
                                                        category_id=category).exists():
        answers = DetectDataSet.objects.get(identify_id=assesment.detect,
                                            sub_category_id=sub_category_id,
                                            category_id=category)
    elif function == 4 and RespondDataSet.objects.filter(identify_id=assesment.respond,
                                                         sub_category_id=sub_category_id,
                                                         category_id=category).exists():
        answers = RespondDataSet.objects.get(identify_id=assesment.respond,
                                             sub_category_id=sub_category_id,
                                             category_id=category)
    elif function == 5 and RecoverDataSet.objects.filter(identify_id=assesment.recover,
                                                         sub_category_id=sub_category_id,
                                                         category_id=category).exists():
        answers = RecoverDataSet.objects.get(identify_id=assesment.recover,
                                             sub_category_id=sub_category_id,
                                             category_id=category)
        print("answers : ", answers)
    # print(subcategory)

    return subcategory, answers


class HomeView(View):

    def get(self, request, function_id=None, category_id=None, sub_category_id=None, direction=None, screen_type=None):
        assesment = findUserAssesmentID(request.user)
        function_id_dict = findFunctionID(assesment)
        print(function_id_dict)
        context = {}
        """If user enter for first time"""
        if not function_id_dict['identify']:
            # create identify
            function_id = Function.objects.get(function_index=1)
            category_id = Category.objects.get(category_index=1)
            sub_category_id = SubCategory.objects.get(subcategory_index=1)

            identify_obj = Identify()
            identify_obj.identify_id = function_id
            identify_obj.category_id = category_id
            identify_obj.save()
            # set identify id to assessment
            assesment.identify = identify_obj
            assesment.save()

        elif function_id is None and category_id is None and sub_category_id is None:
            # direction = "next"
            if function_id_dict['recover']:
                dataset = RecoverDataSet.objects.filter(identify_id=function_id_dict['recover']).order_by(
                    '-sub_category_id__subcategory_index').first()
                function_id = Function.objects.get(function_index=5)
                category_id = Category.objects.get(category_index=dataset.category_id.category_index)
                sub_category_id = SubCategory.objects.get(subcategory_index=dataset.sub_category_id.subcategory_index)
            elif function_id_dict['respond']:
                dataset = RespondDataSet.objects.filter(identify_id=function_id_dict['respond']).order_by(
                    '-sub_category_id__subcategory_index').first()
                function_id = Function.objects.get(function_index=4)
                category_id = Category.objects.get(category_index=dataset.category_id.category_index)
                sub_category_id = SubCategory.objects.get(subcategory_index=dataset.sub_category_id.subcategory_index)
            elif function_id_dict['detect']:
                dataset = DetectDataSet.objects.filter(identify_id=function_id_dict['detect']).order_by(
                    '-sub_category_id__subcategory_index').first()
                function_id = Function.objects.get(function_index=3)
                category_id = Category.objects.get(category_index=dataset.category_id.category_index)
                sub_category_id = SubCategory.objects.get(subcategory_index=dataset.sub_category_id.subcategory_index)
            elif function_id_dict['protect']:
                dataset = ProtectDataSet.objects.filter(identify_id=function_id_dict['protect']).order_by(
                    '-sub_category_id__subcategory_index').first()
                function_id = Function.objects.get(function_index=2)
                category_id = Category.objects.get(category_index=dataset.category_id.category_index)
                sub_category_id = SubCategory.objects.get(
                    subcategory_index=dataset.sub_category_id.subcategory_index)
            elif function_id_dict['identify']:
                if IdentifyDataSet.objects.filter(identify_id=function_id_dict['identify']).exists():
                    dataset = IdentifyDataSet.objects.filter(identify_id=function_id_dict['identify']).order_by(
                        '-sub_category_id__subcategory_index').first()
                    function_id = Function.objects.get(function_index=1)
                    category_id = Category.objects.get(category_index=dataset.category_id.category_index)
                    sub_category_id = SubCategory.objects.get(
                        subcategory_index=dataset.sub_category_id.subcategory_index)
                else:
                    function_id = Function.objects.get(function_index=1)
                    category_id = Category.objects.get(category_index=1)
                    sub_category_id = SubCategory.objects.get(
                        subcategory_index=1)

            # identify_obj = Identify()
            # identify_obj.identify_id = function_id
            # identify_obj.category_id = category_id
            # identify_obj.save()
            # # set identify id to assessment
            # assesment.identify = identify_obj
            # assesment.save()
            # get options
        # if direction == "next":
        if direction:
            function_id = function_id if isinstance(function_id, Function) else Function.objects.get(
                function_index=function_id)
            category_id = category_id if isinstance(category_id, Category) else Category.objects.get(
                category_index=category_id)

            if screen_type == "report":
                sub_category_id = SubCategory.objects.get(subcategory_index=sub_category_id)
                context['subcategory'] = sub_category_id
                context['screen_type'] = screen_type
                context['your_desired_state'] = getYourDesiredState()

                if function_id.function_name == 'IDENTIFY':
                    report = IdentifyDataSet.objects.get(identify_id=assesment.identify,
                                                         sub_category_id=sub_category_id,
                                                         category_id=category_id)
                    if report.desired_state:
                        context['desired_state'] = report.desired_state
                        context['desired_state_severity'] = report.desired_state_severity

                elif function_id.function_name == 'PROTECT':
                    report = ProtectDataSet.objects.get(identify_id=assesment.protect,
                                                        sub_category_id=sub_category_id,
                                                        category_id=category_id)
                    if report.desired_state:
                        context['desired_state'] = report.desired_state
                        context['desired_state_severity'] = report.desired_state_severity

                elif function_id.function_name == 'DETECT':
                    report = DetectDataSet.objects.get(identify_id=assesment.detect,
                                                       sub_category_id=sub_category_id,
                                                       category_id=category_id)
                    if report.desired_state:
                        context['desired_state'] = report.desired_state
                        context['desired_state_severity'] = report.desired_state_severity

                elif function_id.function_name == 'RESPOND':
                    report = RespondDataSet.objects.get(identify_id=assesment.respond,
                                                        sub_category_id=sub_category_id,
                                                        category_id=category_id)
                    if report.desired_state:
                        context['desired_state'] = report.desired_state
                        context['desired_state_severity'] = report.desired_state_severity

                elif function_id.function_name == 'RECOVER':
                    report = RecoverDataSet.objects.get(identify_id=assesment.recover,
                                                        sub_category_id=sub_category_id,
                                                        category_id=category_id)
                    if report.desired_state:
                        context['desired_state'] = report.desired_state
                        context['desired_state_severity'] = report.desired_state_severity

                print(report)
                threat_severity = report.level
                maturity_level = report.Assessed_Maturity_Level_value.option_id.option
                context['threat_severity'] = threat_severity
                context['maturity_level'] = maturity_level
                context['maturity_level_details'] = report.Assessed_Maturity_Level_value.option_id.details
                context['report_id'] = report.dataset_id
                asd_maturity_avg, level_avg = PeerAverage(sub_category_id, function_id)
                context['asd_maturity_avg'] = ThreatScoringTABLE.objects.get(id=asd_maturity_avg)
                context['level_avg'] = level_avg

                return render(request, 'index.html', context)
            elif screen_type == "question" and direction == "next":
                try:
                    sub_category_id = SubCategory.objects.get(subcategory_index=sub_category_id + 1)
                except Exception as e:
                    if sub_category_id + 1 > 108:
                        identify_dataset = IdentifyDataSet.objects.filter(identify_id=assesment.identify)
                        protect_dataset = ProtectDataSet.objects.filter(identify_id=assesment.protect)
                        detect_dataset = DetectDataSet.objects.filter(identify_id=assesment.detect)
                        recover_dataset = RecoverDataSet.objects.filter(identify_id=assesment.recover)
                        respond_dataset = RespondDataSet.objects.filter(identify_id=assesment.respond)
                        print(identify_dataset)
                        from itertools import chain
                        result_list = identify_dataset.union(protect_dataset, detect_dataset, recover_dataset,
                                                             respond_dataset)
                        total_datasets = len(result_list)
                        print(result_list.order_by('-severity'))
                        descending = result_list.order_by('-severity')
                        identify_objs = []
                        protect_objs = []
                        detect_objs = []
                        recover_objs = []
                        respond_objs = []
                        for index, dataset in enumerate(descending):
                            dataset.total = index

                            if dataset.category_id.function_id.function_name == 'IDENTIFY':
                                identify_objs.append(dataset)
                            elif dataset.category_id.function_id.function_name == 'PROTECT':
                                protect_objs.append(dataset)
                            elif dataset.category_id.function_id.function_name == 'DETECT':
                                detect_objs.append(dataset)
                            elif dataset.category_id.function_id.function_name == 'RECOVER':
                                recover_objs.append(dataset)
                            elif dataset.category_id.function_id.function_name == 'RESPOND':
                                respond_objs.append(dataset)

                        IdentifyDataSet.objects.bulk_update(identify_objs, ['total'])
                        ProtectDataSet.objects.bulk_update(protect_objs, ['total'])
                        DetectDataSet.objects.bulk_update(detect_objs, ['total'])
                        RecoverDataSet.objects.bulk_update(recover_objs, ['total'])
                        RespondDataSet.objects.bulk_update(respond_objs, ['total'])

                        print(len(result_list))
                        context = {
                            'identify_dataset': identify_dataset,
                            'protect_dataset': protect_dataset,
                            'detect_dataset': detect_dataset,
                            'recover_dataset': recover_dataset,
                            'respond_dataset': respond_dataset,
                            'total_datasets':total_datasets
                        }

                        return render(request, 'thankyou.html', context)
                    print(e)

            elif screen_type == "question" and direction == "previous":
                sub_category_id = SubCategory.objects.get(subcategory_index=sub_category_id - 1)

        context = getOptions()
        # get first question
        context['screen_type'] = 'question'
        context['subcategory'], context['answers'] = getFistQuestion(function_id, category_id, sub_category_id,
                                                                     assesment, direction)
        print(context)
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        direction = request.POST.get("direction")
        print("direction***", direction)
        screen_type = request.POST.get("screen_type")
        function_id = int(request.POST.get("identify_id"))
        category_id = int(request.POST.get("category_id"))
        subcategory_id = int(request.POST.get("sub_category_id"))

        if direction == "previous":
            return redirect('home',
                            function_id=function_id,
                            category_id=category_id,
                            sub_category_id=subcategory_id,
                            direction="previous", screen_type=screen_type)

        if screen_type == "question":
            return redirect('home',
                            function_id=function_id,
                            category_id=category_id,
                            sub_category_id=subcategory_id,
                            direction="next", screen_type=screen_type)
        assesment = findUserAssesmentID(request.user)
        print(request.POST)
        # int(request.POST.get("assessed-maturity-level"))
        # Identify.objects.get(id=int(request.POST.get("identify_id")))
        function = Function.objects.get(function_id=function_id)
        identify_saved = None
        subcategory_object = SubCategory.objects.get(subcategory_id=subcategory_id)
        category_object = Category.objects.get(category_id=category_id)
        if function.function_name == 'IDENTIFY':
            if IdentifyDataSet.objects.filter(identify_id=assesment.identify,
                                              sub_category_id=subcategory_object,
                                              category_id=category_object).exists():
                identify_saved = IdentifyDataSet.objects.get(identify_id=assesment.identify,
                                                             sub_category_id=subcategory_object,
                                                             category_id=category_object)
            else:
                identify_saved = IdentifyDataSet()
            identify_saved.identify_id = assesment.identify
        elif function.function_name == 'PROTECT':
            if ProtectDataSet.objects.filter(identify_id=assesment.protect,
                                             sub_category_id=subcategory_object,
                                             category_id=category_object).exists():
                identify_saved = ProtectDataSet.objects.get(identify_id=assesment.protect,
                                                            sub_category_id=subcategory_object,
                                                            category_id=category_object)
            else:
                identify_saved = ProtectDataSet()
            identify_saved.identify_id = assesment.protect
            print(identify_saved.identify_id, " identify_saved.identify_id", assesment.protect)
        elif function.function_name == 'DETECT':
            if DetectDataSet.objects.filter(identify_id=assesment.detect,
                                            sub_category_id=subcategory_object,
                                            category_id=category_object).exists():
                identify_saved = DetectDataSet.objects.get(identify_id=assesment.detect,
                                                           sub_category_id=subcategory_object,
                                                           category_id=category_object)
            else:
                identify_saved = DetectDataSet()
            identify_saved.identify_id = assesment.detect
        elif function.function_name == 'RESPOND':
            if RespondDataSet.objects.filter(identify_id=assesment.respond,
                                             sub_category_id=subcategory_object,
                                             category_id=category_object).exists():
                identify_saved = RespondDataSet.objects.get(identify_id=assesment.respond,
                                                            sub_category_id=subcategory_object,
                                                            category_id=category_object)
            else:
                identify_saved = RespondDataSet()
            identify_saved.identify_id = assesment.respond
        elif function.function_name == 'RECOVER':
            if RecoverDataSet.objects.filter(identify_id=assesment.recover,
                                             sub_category_id=subcategory_object,
                                             category_id=category_object).exists():
                identify_saved = RecoverDataSet.objects.get(identify_id=assesment.recover,
                                                            sub_category_id=subcategory_object,
                                                            category_id=category_object)
            else:
                identify_saved = RecoverDataSet()
            identify_saved.identify_id = assesment.recover
        else:
            pass

        identify_saved.category_id = Category.objects.get(category_id=category_id)
        identify_saved.sub_category_id = SubCategory.objects.get(subcategory_id=subcategory_id)
        identify_saved.process_level_value = MeturityScoringTABLE.objects.get(
            option_id__option_id=int(request.POST.get("process-level")))
        identify_saved.policy_level_value = MeturityScoringTABLE.objects.get(
            option_id__option_id=int(request.POST.get("policy-level")))
        identify_saved.Documentation_Level_value = MeturityScoringTABLE.objects.get(
            option_id__option_id=int(request.POST.get("documentation"
                                                      "-level")))
        identify_saved.Automation_Level_value = MeturityScoringTABLE.objects.get(
            option_id__option_id=int(request.POST.get("automation-level")))
        identify_saved.Primary_Threat_value = ThreatScoringTABLE.objects.get(
            option_id__option_id=int(request.POST.get("primary-threat")))
        identify_saved.Likelihood_of_Threat_value = ThreatScoringTABLE.objects.get(
            option_id__option_id=int(request.POST.get("likelihood")))
        identify_saved.Impact_of_Threat_Occurrence_value = ThreatScoringTABLE.objects.get(
            option_id__option_id=int(request.POST.get("impact")))
        identify_saved.save()

        # identify_saved.Assessed_Maturity_Level_value = ThreatScoringTABLE.objects.get(option_id__option_id=2)
        # identify_saved.save()
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

        if function.function_name == 'IDENTIFY':
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
        elif function.function_name == 'PROTECT':
            identify_maturity_roadmap_instance = ProtectMaturityRoadMap.objects.create(
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
                dataset_id=ProtectDataSet.objects.get(dataset_id=identify_saved.dataset_id),
            )
        elif function.function_name == 'DETECT':
            print(identify_saved.identify_id, "****")
            identify_maturity_roadmap_instance = DetectMaturityRoadMap.objects.create(
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
                dataset_id=DetectDataSet.objects.get(dataset_id=identify_saved.dataset_id),
            )
        elif function.function_name == 'RESPOND':
            identify_maturity_roadmap_instance = RespondMaturityRoadMap.objects.create(
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
                dataset_id=RespondDataSet.objects.get(dataset_id=identify_saved.dataset_id),
            )
        elif function.function_name == 'RECOVER':
            identify_maturity_roadmap_instance = RecoverMaturityRoadMap.objects.create(
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
                dataset_id=RecoverDataSet.objects.get(dataset_id=identify_saved.dataset_id),
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

        return redirect('home',
                        function_id=function_id,
                        category_id=category_id,
                        sub_category_id=subcategory_id,
                        direction="next", screen_type=screen_type)
