"""pyVue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import re_path
from django.views.generic.base import TemplateView
from django.urls import path
# 导入swagger的两个Render类
from rest_framework_swagger.renderers import SwaggerUIRenderer,OpenAPIRenderer
from api import urls
from rest_framework import routers
# 重要的是如下三行
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from django.conf.urls import url
# from pyVue.views import SwaggerSchemaView,ReturnJson,StudentsApiView
# 利用get_schema_view()方法，传入两个Render类得到一个schema view
schema_view = get_schema_view(title='API',renderer_classes=[SwaggerUIRenderer,OpenAPIRenderer])

# # 路由
# router = routers.DefaultRouter()
# router.register(r'users',views.UserViewSet,base_name='user')
# router.register(r'groups',views.GroupViewSet,base_name='group')


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',TemplateView.as_view(template_name='index.html')),
    # 访问localhost:8000/docs/即可
    path('docs/', schema_view, name='swagger接口文档'), #swagger接口文档路由
    path('api/', include("api.urls"))

]

