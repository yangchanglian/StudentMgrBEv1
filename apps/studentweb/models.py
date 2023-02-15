from django.db import models

# ---学生管理系统Vs models
# 学院 faculty  ，专业 major  学生信息 student

# ====学院 ---Faculty:Id,name
class Faculty(models.Model):
    name = models.CharField(verbose_name="学院名称",max_length=100,unique=True,null=False,blank=False)

    class Meta:
        managed = True
        app_label = "studentweb"
        db_table = "stu_Faculty"
    def __str__(self):
        return "%s" %(self.name)

# ====专业---Major:id,name,faculty
class Major(models.Model):
    name = models.CharField(verbose_name="专业名称",max_length=100,null=False,blank=False)
    faculty = models.ForeignKey(verbose_name="所属学院",to=Faculty,on_delete=models.PROTECT)

    class Meta:
        managed = True
        app_label = "studentweb"
        db_table = "stu_Major"
    def __str__(self):
        return "%s" %(self.name)
# ====学生信息 --Student:sno,name,gender,brithday,major,email,address,image
class Student(models.Model):
    sno = models.CharField(verbose_name="学号",max_length=100,primary_key=True,null=False,blank=False)
    name = models.CharField(verbose_name="姓名",max_length=100,null=False,blank=False)
    gender = models.CharField(verbose_name="性别",max_length=100,null=True,blank=True,default=None)
    birthday = models.DateField(verbose_name="出生日期",null=True,blank=True,default=None)
    major = models.ForeignKey(verbose_name="专业",to=Major,on_delete=models.PROTECT)
    mobile = models.CharField(verbose_name="电话",max_length=100,null=True,blank=True,default=None)
    email = models.CharField(verbose_name="邮箱", max_length=100, null=True, blank=True, default=None)
    address = models.CharField(verbose_name="地址", max_length=100, null=True, blank=True, default=None)
    image = models.CharField(verbose_name="照片", max_length=100, null=True, blank=True, default=None)

    class Meta:
        managed = True
        app_label = "studentweb"
        db_table = "stu_Student"
    def __str__(self):
        return "%s" %(self.name)