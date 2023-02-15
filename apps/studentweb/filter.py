# =======导入模块 ================
from django_filters import FilterSet,filters
from studentweb.models import Faculty,Major,Student

# -----Faculty的Filter类 ----
class FacultyFilter(FilterSet):
    # 重写需要支持模糊匹配的字段
    name = filters.CharFilter(field_name='name',lookup_expr="icontains")

    class Meta:
        model = Faculty
        fields = ('name',)

# -----Major的Filter类----
class MajorFilter(FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr="icontains")
    class Meta:
        model = Major
        fields = ('name','faculty')

# ------student的Filter类 ------
class StudentFilter(FilterSet):
    sno = filters.CharFilter(field_name='sno', lookup_expr="icontains")
    name = filters.CharFilter(field_name='name', lookup_expr="icontains")
    moblie = filters.CharFilter(field_name='moblie', lookup_expr="icontains")
    major = filters.CharFilter(field_name='major')
    faculty = filters.CharFilter(field_name='major__faculty')
    class Meta:
        model = Student
        fields = ('sno','name','mobile','mobile','major','faculty')