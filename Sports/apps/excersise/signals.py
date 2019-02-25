# _*_ coding: utf-8 _*_
# @time     : 2018/11/22
# @Author   : Amir
# @Site     : 
# @File     : signals.py
# @Software : PyCharm

from django.conf import settings
from .models import Schedule, JoinSchedule
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import JoinSchedule


# 通过信号实现人数加一
@receiver(post_save, sender=JoinSchedule)
def create_userfav(sender, instance=None, created=False, **kwargs):
    if created:
        schedule = instance.schedule
        if schedule.now_people < schedule.people_nums:
            schedule.now_people += 1
            schedule.save()
        else:
            pass


# 通过信号实现人数减一
@receiver(post_delete, sender=JoinSchedule)
def delete_userfav(sender, instance=None, created=False, **kwargs):
    schedule = instance.schedule
    schedule.now_people -= 1
    schedule.save()