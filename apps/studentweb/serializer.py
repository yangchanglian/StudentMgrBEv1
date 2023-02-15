# =============导入模块 =================
from rest_framework import serializers
from studentweb.models import Faculty,Major,Student

# -----Faculty序列化类----
class FacultySerialzer(serializers.ModelSerializer):

    class Meta:
        model = Faculty
        fields = "__all__"
# -----Major序列化类----
class MajorSerialzer(serializers.ModelSerializer):
    faculty = FacultySerialzer()
    class Meta:
        model = Major
        fields = "__all__"

# -----Student序列化类----
class StudentSerialzer(serializers.ModelSerializer):
    major = MajorSerialzer()
    class Meta:
        model = Student
        fields = "__all__"