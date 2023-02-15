"""
本模板实现文件的上传：图片，视频，excel等
当前的上传任务通过update_file实现，update_file中有三个参数，分别为：
1）file ----提交的文件
2）path ----存储的子目录
3）type ----文件名的类型
    1 ----时间 +随机值
    2 ---- uuid
返回值的描述：
成功：status:True,Data:新写入的文件名
失败： status:False,error:错误描述


"""
# =======导入模块 ==========
from datetime import datetime
import random
import uuid
from django.conf import settings
import os
def get_file_name_random_date():
    """根据日期获取随机值"""
    filename = datetime.now().strftime("%Y-%m-%d").replace("-","")
    filename += str(random.randint(1000,9999))
    return filename

def update_file(file,path:str,type:int):
    """..."""
    # 定义一个new_name获取新路径
    new_name = ""
    # 判断
    if type == 1:
        new_name = get_file_name_random_date()
    elif type == 2:
        new_name = uuid.uuid4().hex

    # 拼接路径
    file_name = settings.MEDIA_ROOT + os.path.sep + path + os.path.sep + new_name + os.path.splitext(file.name)[1]
    # 开始写入
    try:
        f = open(file_name,'wb')
        # 分多次写入
        for i in file.chunks():
            f.write(i)
        # 关闭
        f.close()
        # 返回
        return {'status': True, 'data':new_name + os.path.splitext(file.name)[1]}
    except Exception as e:
        return {'status':False,'error':"文件写入磁盘出现异常"}