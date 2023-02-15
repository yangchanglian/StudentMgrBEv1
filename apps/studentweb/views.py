# ==========导入模块 ==============
from rest_framework.viewsets import ModelViewSet # 封装完成的Modelviewset 视图集
from studentweb.models import Faculty,Major,Student # 具体的类
from studentweb.serializer import FacultySerialzer,MajorSerialzer,StudentSerialzer # 序列化类
from django_filters.rest_framework import DjangoFilterBackend # 实现筛选的后台模块
from studentweb.filter import FacultyFilter,MajorFilter,StudentFilter # 导入筛选类
from rest_framework.filters import SearchFilter # 导入搜索的后台功能
from studentweb.paginations import MyPageNumberPagintion
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from utils import myupload
# ----Faculty视图---
class FacultyViewSet(ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerialzer

    # 指定筛选类
    filter_class = FacultyFilter

# ----Major视图---
class MajorViewSet(ModelViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorSerialzer

    # 指定筛选类
    filter_class = MajorFilter

# ----Student视图---
class StudentViewSet(ModelViewSet):
    """
       create:
       创建学生信息
       retrieve:
       获取学生信息详情数据
       update:
       完整更新学生信息
       partial_update:
       部分更新学生信息
       destroy:
       删除学生信息
       list:
       获取所有学生信息

       """

    queryset = Student.objects.all()
    serializer_class = StudentSerialzer
    pagination_class = MyPageNumberPagintion # 分页
    # 指定筛选类
    filter_class = StudentFilter
    # 指定查找匹配的字段
    search_fields = ('sno','name','mobile','email','address')

    def create(self, request, *args, **kwargs):
        # 接收传递的值
        rec = request.data
        # 添加
        try:
            Student.objects.create(sno=rec.get('sno'),name=rec.get('name'),gender=rec.get('gender'),
                                   birthday=rec.get('birthday'),major_id=rec.get('major'),mobile=rec.get('mobile'),
                                   email=rec.get('email'),address=rec.get('address'),image=rec.get('image'))
            return Response({'msg': '添加成功'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error':'添加学生失败'},status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        # 接收传递的值
        rec = request.data
        # 添加
        try:
            Student.objects.filter(pk=kwargs.get('pk')).update(name=rec.get('name'),gender=rec.get('gender'),
                                   birthday=rec.get('birthday'),major_id=rec.get('major'),mobile=rec.get('mobile'),
                                   email=rec.get('email'),address=rec.get('address'),image=rec.get('image'))
            return Response({'msg': '修改成功'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error':'修改学生失败'},status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post','get'],detail=False)
    def upload(self,request, *args, **kwargs):
        # 接收前端传递的文件
        rev_file = request.FILES.get('file')
        # 判断是否出错
        if not rev_file:
            return Response(status=status.HTTP_400_BAD_REQUEST)
         # 调用
        res = myupload.update_file(rev_file,'images',2)
        # 返回
        return Response(res)



