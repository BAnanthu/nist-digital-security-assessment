import os
import sqlite3

from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from Smarthive.settings import BASE_DIR
from category.models import SubCategory
from dashboard.forms import SubCategoryForm, LevelsForm
from function.models import Function
from questions.models import Levels, Options
from report.data_model import MeturityScoringTABLE, ThreatScoringTABLE
from report.models import Assesmeent, IdentifyDataSet, ProtectDataSet, DetectDataSet, RespondDataSet, RecoverDataSet


class Dashboard(View):

    def get(self, request):
        template = 'dashboard/dashboard-main.html'
        context = {}
        return render(request, template, context)


class SubCategoriesListView(View):
    def get(self, request):
        subcategories = SubCategory.objects.all()
        template = 'questions/list_subcategories.html'
        context = {"subcategories": subcategories}
        return render(request, template, context)


class SubCategoriesEditView(View):

    @staticmethod
    def post(request, pk):
        form = SubCategoryForm(request.POST)

        if form.is_valid():
            SubCategory.objects.filter(pk=pk).update(subcategory_index=request.POST['subcategory_index'],
                                                     function_id=request.POST['function_id'],
                                                     subcategory_name=request.POST['subcategory_name'],
                                                     subcategory_details=request.POST['subcategory_details'],
                                                     category_id=request.POST['category_id'])
            messages.success(request, f'Sub Category with id({pk}) is updated successfully')

        return redirect('sub_categories_edit', pk=pk)

    @staticmethod
    def get(request, pk):
        template = 'questions/edit_subcategory.html'
        sub_category = SubCategory.objects.get(subcategory_id=pk)
        form = SubCategoryForm(initial={'subcategory_index': sub_category.subcategory_index,
                                        'function_id': sub_category.function_id,
                                        'subcategory_name': sub_category.subcategory_name,
                                        'subcategory_details': sub_category.subcategory_details,
                                        'category_id': sub_category.category_id})
        context = {'form': form, 'sub_category': sub_category, 'pk': pk}
        return render(request, template, context)


class QuestionsListView(View):
    def get(self, request):
        questions = Levels.objects.all()
        template = 'questions/list_questions.html'
        context = {"questions": questions}
        return render(request, template, context)


class QuestionsEditView(View):
    @staticmethod
    def post(request, pk):
        form = LevelsForm(request.POST)
        if form.is_valid():
            Levels.objects.filter(pk=pk).update(level_name=request.POST['level_name'],
                                                level_details=request.POST['level_details'],
                                                score_type=request.POST['score_type'])
            messages.success(request, f'Question with id({pk}) is updated successfully')

        return redirect('question_edit', pk=pk)

    @staticmethod
    def get(request, pk):
        template = 'questions/edit_question.html'
        level = Levels.objects.get(level_id=pk)
        options = Options.objects.filter(level_id=pk)
        form = LevelsForm(initial={'level_name': level.level_name,
                                   'level_details': level.level_details,
                                   'score_type': level.score_type})
        context = {'form': form, 'level': level, 'options': options, 'pk': pk}
        return render(request, template, context)


class OptionEditView(View):
    pass


class AssesmentsListView(View):
    def get(self, request):
        assessments = Assesmeent.objects.all()
        template = 'assessments/list_assesment.html'
        context = {"assessments": assessments}
        return render(request, template, context)


class AssesmentsView(View):
    def get(self, request, id):
        # user = User.objects.get(id=id)
        assessments = Assesmeent.objects.get(assessment_id=id)
        template = 'assessments/assesment_view.html'
        context = {"username": assessments.user_id.username,
                   "identify": assessments.identify,
                   "protect": assessments.protect,
                   "detect": assessments.detect,
                   "respond": assessments.respond,
                   "recover": assessments.recover,
                   }
        # return render(request, template, context)
        return render(request, template, context)


class AssesmentsCategoryListView(View):
    def get(self, request, id, fu_id):
        identify = {}
        categories = Category.objects.filter(function_id=fu_id)
        function = Function.objects.get(function_id=fu_id)
        print("*******function******", function)
        if function.function_name == 'IDENTIFY':
            for category in categories:
                identify[category.category_name] = IdentifyDataSet.objects.filter(identify_id=id, category_id=category)
        elif function.function_name == 'PROTECT':
            print("*************",id)
            for category in categories:
                identify[category.category_name] = ProtectDataSet.objects.filter(identify_id=id, category_id=category)
        elif function.function_name == 'DETECT':
            for category in categories:
                identify[category.category_name] = DetectDataSet.objects.filter(identify_id=id, category_id=category)
        elif function.function_name == 'RESPOND':
            for category in categories:
                identify[category.category_name] = RespondDataSet.objects.filter(identify_id=id, category_id=category)
        elif function.function_name == 'RECOVER':
            for category in categories:
                identify[category.category_name] = RecoverDataSet.objects.filter(identify_id=id, category_id=category)
        else:
            pass

        template = 'assessments/categories_list_view.html'
        context = {"identify": identify}
        print(context)
        # return render(request, template, context)
        return render(request, template, context)


def setupFunctions(cursor):
    try:
        sqlite_select_query = """SELECT * from function_function"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            Function.objects.create(
                # function_id=row[0],
                function_index=row[1],
                function_name=row[2],
                function_details=row[3],
            )
        return "SUCCESS"
    except Exception as e:
        return e


from category.models import SubCategory, Category


def setupCategory(cursor):
    try:
        sqlite_select_query = """SELECT * from category_category"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print(row)
            Category.objects.create(
                # category_id=row[0],
                category_index=row[1],
                function_id=Function.objects.get(function_id=row[5]),
                category_name=row[2],
                category_tag=row[3],
                category_details=row[4],
            )
        return "SUCCESS"
    except Exception as e:
        return e


def setupSubcategory(cursor):
    try:
        sqlite_select_query = """SELECT * from category_subcategory"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print(row)
            SubCategory.objects.create(
                # subcategory_id=row[0],
                subcategory_index=row[1],
                category_id=Category.objects.get(category_id=row[4]),
                function_id=Function.objects.get(function_id=row[5]),
                subcategory_name=row[2],
                subcategory_details=row[3],
            )
        return "SUCCESS"
    except Exception as e:
        return e


def setupLevels(cursor):
    try:
        sqlite_select_query = """SELECT * from questions_levels"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print(row)
            Levels.objects.create(
                # level_id=row[0],
                level_name=row[1],
                level_details=row[3],
                score_type=row[2]
            )
        return "SUCCESS"
    except Exception as e:
        return e


def setupOptions(cursor):
    try:
        sqlite_select_query = """SELECT * from questions_options"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print(row)
            Options.objects.create(
                # option_id=row[0],
                level_id=Levels.objects.get(level_id=row[2]),
                option=row[1]
            )
        return "SUCCESS"
    except Exception as e:
        return e


def setupMeturityScoringTABLE(cursor):
    try:
        sqlite_select_query = """SELECT * from report_meturityscoringtable"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print(row)
            MeturityScoringTABLE.objects.create(
                # id=row[0],
                level_id=Levels.objects.get(level_id=row[2]),
                option_id=Options.objects.get(option_id=row[3]),
                value=row[1],
            )
        return "SUCCESS"
    except Exception as e:
        return e


def setupThreatScoringTABLE(cursor):
    try:
        sqlite_select_query = """SELECT * from report_threatscoringtable"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print(row)
            ThreatScoringTABLE.objects.create(
                # id=row[0],
                level_id=Levels.objects.get(level_id=row[2]),
                option_id=Options.objects.get(option_id=row[3]),
                value=row[1],
            )
        return "SUCCESS"
    except Exception as e:
        return e


def setupdatabase(request):
    conn = None
    context = {}
    db_file = os.path.join(BASE_DIR, 'db.sqlite3')
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        context['setupFunctions'] = setupFunctions(cursor)
        context['setupCategory'] = setupCategory(cursor)
        context['setupSubcategory'] = setupSubcategory(cursor)
        context['setupLevels'] = setupLevels(cursor)
        context['setupOptions'] = setupOptions(cursor)
        context['setupMeturityScoringTABLE'] = setupMeturityScoringTABLE(cursor)
        context['setupThreatScoringTABLE'] = setupThreatScoringTABLE(cursor)
        cursor.close()
    except Exception as e:
        print(e)

    return JsonResponse(context)
