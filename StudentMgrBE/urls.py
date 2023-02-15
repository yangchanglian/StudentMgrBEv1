"""StudentMgrBE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
# =====导入URL允许访问所有的文件上传======
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
openapi.Info(
title="API接口文档平台",    # 必传
default_version='v1',   # 必传
description="这是一个接口文档",
terms_of_service="",
contact=openapi.Contact(email="651205558@qq.com"),
license=openapi.License(name="BSD License"),
),
public=True,
#permission_classes=(permissions.AllowAny,),   # 权限类py
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('studentweb.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)