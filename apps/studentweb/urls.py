# =============导入模块 ============
from django.urls import path
from rest_framework.routers import DefaultRouter
from studentweb.views import FacultyViewSet,MajorViewSet,StudentViewSet
# ======1.实例化一个 DefaultRouter ===
router = DefaultRouter()
# ======2.注册相应的url==========
#注册faculty对象
router.register('facultys',FacultyViewSet,basename='facultys')
# 注册major对象
router.register('majors',MajorViewSet,basename='majors')
# 注册student对象
router.register('students',StudentViewSet,basename='students')
urlpatterns = [

]
# ========3.附加到urlpatterns集合中 =======
urlpatterns += router.urls