# _*_ coding: utf-8 _*_
# @time     : 2018/11/22
# @Author   : Amir
# @Site     : 
# @File     : current.py
# @Software : PyCharm

from rest_framework.compat import unicode_to_repr


# 自定义
class CurrentSchoolDefault(object):
    def set_context(self, serializer_field):
        self.school = serializer_field.context['request'].user.school

    def __call__(self):
        return self.school

    def __repr__(self):
        return unicode_to_repr('%s()' % self.__class__.__name__)


# # CurrentUserDefault 源码
# class CurrentUserDefault(object):
#     def set_context(self, serializer_field):
#         self.user = serializer_field.context['request'].user
#
#     def __call__(self):
#         return self.user
#
#     def __repr__(self):
#         return unicode_to_repr('%s()' % self.__class__.__name__)
