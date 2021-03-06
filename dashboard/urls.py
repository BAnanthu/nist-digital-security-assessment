from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name="dashboard"),
    path('sub-categories-list', views.SubCategoriesListView.as_view(), name="sub_categories_list"),
    path('sub-categories-edit/<int:pk>', views.SubCategoriesEditView.as_view(), name="sub_categories_edit"),
    path('questions', views.QuestionsListView.as_view(), name="questions_list"),
    path('question/<int:pk>', views.QuestionsEditView.as_view(), name="question_edit"),
    path('option/<int:pk>', views.OptionEditView.as_view(), name="option_edit"),
    # path('setupdatabase/', views.setupdatabase),
    path('assessment-list', views.AssesmentsListView.as_view(), name="assessment_list"),
    path('assessment-view/<int:id>', views.AssesmentsView.as_view(), name="assessment_view"),
    path('assessment-category-list/<int:id>/<int:fu_id>', views.AssesmentsCategoryListView.as_view(), name="assessment_category_list"),
    path('assessment-view-print/', views.AssesmentsViewPrintView.as_view(), name="assessments_view_print"),

]
