from rest_framework import serializers

from category.models import SubCategory
from function.models import Identify, Function
from questions.models import Levels, Options

class FunctionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Function
        fields = '__all__'


class OptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Options
        fields = '__all__'
        # fields = ['option_id','option']

class LevelSerializer(serializers.ModelSerializer):
    option = OptionsSerializer(many=True, read_only=True)

    class Meta:
        model = Levels
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    Answer = serializers.SerializerMethodField()  # add field
    Options = serializers.SerializerMethodField()  # add field
    Type = serializers.SerializerMethodField()  # add field
    function_id = serializers.SerializerMethodField()  # add field
    function_name = serializers.SerializerMethodField()  # add field
    category_name = serializers.SerializerMethodField()  # add field


    # def __init__(self,*args,**kwargs):
    #     self.catedoryId = 0

    class Meta:
        model = SubCategory
        fields = ['Type','function_id','function_name', 'category_id', 'category_name','subcategory_id',
                  'subcategory_index', 'subcategory_name',
                  'subcategory_details', 'Answer', 'Options']
        # fields = '__all__'

    def get_Answer(self, obj):
        # print(obj.category_id.category_id)
        levels = Levels.objects.all()
        # here write the logic to compute the value based on object
        return [0 for i in range(len(levels))]

    def get_Options(self, obj):
        levels = Levels.objects.all()
        s = LevelSerializer(levels, many=True)
        # here write the logic to compute the value based on object
        return s.data

    def get_Type(self, obj):
        # here write the logic to compute the value based on object
        return "question"

    def get_function_id(self, obj):
        # here write the logic to compute the value based on object
        return obj.category_id.function_id.function_id

    def get_function_name(self, obj):
        # here write the logic to compute the value based on object
        return obj.category_id.function_id.function_name

    def get_category_name(self, obj):
        # here write the logic to compute the value based on object
        return obj.category_id.category_name


    # def get_tracks(self, obj):
    #     serializer = SubCategorySerializer(obj.tracks, many=True)
    #     return {'items': serializer.data}


