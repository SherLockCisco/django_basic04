from django.db import models

# Create your models here.


#模型类继承自Models
'''
字段 
    字段名 = model。类型（选项）
    
    数据表的字段名，不要使用python mysql关键字
    
'''
class MediaclRecord(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


#用户
class UserUni(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    #外键约束
    mediaclRecord = models.ForeignKey(MediaclRecord,on_delete=models.CASCADE)