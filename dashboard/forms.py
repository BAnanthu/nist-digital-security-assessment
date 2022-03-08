from django import forms
from django.forms import ModelForm

from category.models import SubCategory
from questions.models import Levels


class SubCategoryForm(ModelForm):

    class Meta:
        model = SubCategory
        labels = {
            "subcategory_index": "Index",
            "category_id": "category",
            "function_id": "function",
            "subcategory_name": "Index",
        }
        fields = ['subcategory_index', 'function_id', 'category_id','subcategory_name','subcategory_details']
        widgets = {
            'subcategory_index': forms.TextInput(attrs={'class': 'form-control',
                                                    'aria-expanded': "false",
                                                    'tabindex': "0",
                                                    'aria-haspopup': "true",
                                                    'role': "combobox",
                                                    'data-plugin': "customselect",
                                                        'readonly': 'readonly'
                                                    }),

            'subcategory_name': forms.TextInput(attrs={'class': 'form-control',
                                                    'aria-expanded': "false",
                                                    'tabindex': "0",
                                                    'aria-haspopup': "true",
                                                    'role': "combobox",
                                                    'data-plugin': "customselect"
                                                    }),

            'function_id': forms.Select(attrs={'class': 'form-control',
                                              'aria-expanded': "false",
                                              'tabindex': "0",
                                              'aria-haspopup': "true",
                                              'role': "combobox",
                                              'data-plugin': "customselect"
                                              }),

            'category_id': forms.Select(attrs={'class': 'form-control',
                                               'aria-expanded': "false",
                                               'tabindex': "0",
                                               'aria-haspopup': "true",
                                               'role': "combobox",
                                               'data-plugin': "customselect"
                                               }),

            'subcategory_details': forms.Textarea(attrs={'class': 'form-control',
                                                       'aria-expanded': "false",
                                                       'tabindex': "0",
                                                       'aria-haspopup': "true",
                                                       'role': "combobox",
                                                       'data-plugin': "customselect"
                                                       }),

        }



class LevelsForm(ModelForm):

    class Meta:
        model = Levels
        labels = {
            "level_name": "name",
            "level_details": "details",
            "score_type": "type",
        }
        fields = ['level_name', 'level_details','score_type']
        widgets = {
            'level_name': forms.TextInput(attrs={'class': 'form-control',
                                                    'aria-expanded': "false",
                                                    'tabindex': "0",
                                                    'aria-haspopup': "true",
                                                    'role': "combobox",
                                                    'data-plugin': "customselect"
                                                    }),


            'score_type': forms.Select(attrs={'class': 'form-control',
                                              'aria-expanded': "false",
                                              'tabindex': "0",
                                              'aria-haspopup': "true",
                                              'role': "combobox",
                                              'data-plugin': "customselect"
                                              }),

            'level_details': forms.Textarea(attrs={'class': 'form-control',
                                                       'aria-expanded': "false",
                                                       'tabindex': "0",
                                                       'aria-haspopup': "true",
                                                       'role': "combobox",
                                                       'data-plugin': "customselect"
                                                       }),

        }
