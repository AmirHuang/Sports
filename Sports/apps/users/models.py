from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

from schools.models import Schools


class UserProfile(AbstractUser):
    # 用户表
    name = models.CharField('姓名', max_length=30, null=True, blank=True)
    image = models.ImageField('头像', upload_to='users/', default='', null=True, blank=True)
    birthday = models.DateField('出生年月', null=True, blank=True)
    mobile = models.CharField('电话', max_length=11, null=True, blank=True)
    student_id = models.CharField('学号', max_length=32, default='', null=True, blank=True)
    gender = models.CharField('性别', choices=(('male', '男'), ('famale', '女')), default='', null=True, blank=True,
                              max_length=6)
    email = models.EmailField('邮箱')
    school = models.ForeignKey(Schools, verbose_name='学校', on_delete=models.CASCADE, null=True, blank=True)
    institude = models.ForeignKey(Schools, verbose_name='学院', on_delete=models.CASCADE, related_name='institude',
                                  null=True, blank=True)
    profession = models.ForeignKey(Schools, verbose_name='专业', on_delete=models.CASCADE, related_name='profession',
                                   null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta():
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.username


class VerifyCode(models.Model):
    # 短信验证码
    code = models.CharField(max_length=10, verbose_name='短信验证码')
    mobile = models.CharField(max_length=11, verbose_name='电话')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta():
        verbose_name = '短信验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code


