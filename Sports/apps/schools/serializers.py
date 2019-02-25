# _*_ coding: utf-8 _*_
# @Time     : 11:45
# @Author   : Amir
# @Site     : 
# @File     : serializers.py
# @Software : PyCharm

from rest_framework import serializers

from .models import *


class SchoolSerializer1(serializers.ModelSerializer):

    class Meta:
        model = Schools
        fields = ('name', 'category_type', 'sub_cat', 'add_time')


class SchoolSerializer2(serializers.ModelSerializer):
    sub_cat = SchoolSerializer1(many=True)

    class Meta:
        model = Schools
        fields = ('name', 'category_type', 'sub_cat', 'add_time')


class SchoolSerializer3(serializers.ModelSerializer):
    sub_cat = SchoolSerializer2(many=True)

    class Meta:
        model = Schools
        fields = '__all__'

