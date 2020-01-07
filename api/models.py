from django.db import models
# Create your models here.

class Case(models.Model):
    casename = models.CharField('用例标题',max_length=64) #用例名称
    casedesc = models.CharField('用例描述',max_length=200) #用例描述，或者脚本
    case_type = models.CharField('用例类型',max_length=100)#用例类型
    case_creater = models.CharField('创建者',max_length=200,null=True) #产品负责人
    create_time = models.DateTimeField('创建时间',auto_now=True) #创建时间，自动获取当前时间
    result = models.CharField('执行结果',max_length=100)#执行结果

    class Meta:
        db_table = 'case' #指定数据库表名
        verbose_name = '用例管理' #在admin站点中显示名称
        verbose_name_plural = '用例管理'  #显示得复数名称

    def __str__(self):
        return self.productname