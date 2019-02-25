"""Sports URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.urls import path, include, re_path
from django.views.static import serve
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from Sports.settings import MEDIA_ROOT
from excersise.views import SportsViewset, ScheduleViewset, JoinScheduleViewset, FavViewset
from schools.views import SchoolViewset
from users.views import SmsCodeViewset, UserViewset, SmsCodeViewset

router = DefaultRouter()
# 配置短信验证接口
router.register(r'codes', SmsCodeViewset, base_name='codes')
# 配置运动相关url
router.register(r'sports', SportsViewset, base_name='sports')
# 配置与学校相关url
router.register(r'schools', SchoolViewset, base_name='schools')
# 配置users验证码的url
router.register(r'codes', SmsCodeViewset, base_name='codes')
# 配置users注册的url
router.register(r'users', UserViewset, base_name='users')
# 配置约运动的接口
router.register(r'schedules', ScheduleViewset, base_name='schedules')
# 配置加入的约运动的url接口
router.register(r'my', JoinScheduleViewset, base_name='my')
# 配置喜爱的运动接口
router.register(r'favsports', FavViewset, base_name='favsports')

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),

    # 文件
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),

    path('api-auth/', include('rest_framework.urls')),

    path('', include(router.urls)),

    path('api-token-auth/', views.obtain_auth_token),

    # jwt的token认证接口
    path('login/', obtain_jwt_token)
]
