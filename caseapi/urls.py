from django.urls import include, path
from rest_framework import routers
from caseapi import caseviews

router = routers.DefaultRouter()
router.register(r'users', caseviews.UserViewSet)
router.register(r'groups', caseviews.GroupViewSet)

# 使用自动路由 URL
# 还有登录 URL
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))


]
