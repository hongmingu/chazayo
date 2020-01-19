from rest_framework import serializers
from .models import *

class InfobaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoBase
        fields = ['user', 'nickname', 'phone', 'telephone', 'email',
                  'name', 'sex', 'is_married', 'born', 'country',
                  'address', 'school_base', 'school_kinder', 'school_kinder_in', 'school_kinder_out',
                  'school_middle', 'school_middle_in', 'school_middle_out', 'school_high', 'school_high_in',
                  'school_high_out', 'school_university', 'school_university_in', 'school_university_out', 'school_graduate',
                  'school_graduate_in', 'school_graduate_out', 'appearance', 'appearance_explanation', 'updated',
                  'created']

class ArmyphotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArmyPhoto
        fields = ['user', 'file_50', 'file_300', 'updated', 'created']

class FamilyphotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyPhoto
        fields = ['user', 'file_50', 'file_300', 'updated', 'created']

class SchoolphotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolPhoto
        fields = ['user', 'file_50', 'file_300', 'updated', 'created']

class SchoolinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolInfo
        fields = ['user', 'school_kinder', 'school_kinder_in', 'school_kinder_out', 'school_middle',
                  'school_middle_in', 'school_middle_out', 'school_high', 'school_high_in', 'school_high_out',
                  'school_university', 'school_university_in', 'school_university_out', 'school_graduate', 'school_graduate_in',
                  'school_graduate_out', 'story', 'updated', 'created']

class FamilyinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyInfo
        fields = ['user', 'break_address', 'break_type', 'break_date', 'story',
                  'updated', 'created']

class ArmyinfoSerailizer(serializers.ModelSerializer):
    class Meta:
        model = ArmyInfo
        fields = ['user', 'army_sort', 'army_in', 'army_out', 'army_address',
                  'army_name', 'story', 'updated', 'created']