from django.db import models


# Create your models here.
class UserInfo(models.Model):
    """用户表()"""
    name = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    age = models.IntegerField(verbose_name='年龄')
    phone = models.CharField(verbose_name='电话', max_length=32, default='')

class Classification(models.Model):
    """分类表(用于存储文章分类信息)"""
    name = models.CharField(verbose_name='分类名称', max_length=32)
    description = models.CharField(verbose_name='分类描述', max_length=64)

class Page(models.Model):
    """页面表(用于存储页面信息)"""
    title = models.CharField(verbose_name='页面标题', max_length=32)
    content = models.CharField(verbose_name='内容', max_length=64)

class Journal(models.Model):
    """日志表(用于存储系统日志信息)"""
    type = models.CharField(verbose_name='日志类型', max_length=32)
    content = models.CharField(verbose_name='日志内容', max_length=64)
    time = models.DateTimeField(verbose_name='日志时间')

class Record(models.Model):
    """访问记录表（用于存储用户访问网站的记录信息）"""
    ip = models.IntegerField(verbose_name='IP地址', max_length=32)
    time = models.DateTimeField(verbose_name='访问时间')

class Bug(models.Model):
    """漏洞列表表（包含所有已知的漏洞信息）"""
    type = models.CharField(verbose_name='漏洞类型', max_length=16)
    grade = models.CharField(verbose_name='风险等级', max_length=16)
    cve = models.IntegerField(verbose_name='CVE编号', max_length=32)
    edition = models.CharField(verbose_name='受影响的软件版本', max_length=32)
class Target(models.Model):
    """目标列表表"""
    ip = models.IntegerField(verbose_name='IP地址', max_length=32)
    domain = models.CharField(verbose_name='域名', max_length=32)
    port = models.IntegerField(verbose_name='端口信息', max_length=8)
class Scanningresult(models.Model):
    """扫描结果表（包含每个目标的扫描结果）"""
    name = models.CharField(verbose_name='漏洞名称', max_length=16)
    description = models.CharField(verbose_name='漏洞描述', max_length=64)
    advice = models.CharField(verbose_name='修复建议', max_length=64)
class Scanningjournal(models.Model):
    """扫描日志表"""
    operation = models.CharField(verbose_name='扫描过程中的操作', max_length=32)
    errormessage = models.CharField(verbose_name='错误信息', max_length=16)
    warningmessage = models.CharField(verbose_name='警告信息', max_length=16)
class Operatingrecord(models.Model):
    """操作记录表(记录扫描工具的使用情况)"""
    personnel = models.CharField(verbose_name='扫描人员', max_length=8)
    time = models.DateTimeField(verbose_name='扫描时间')
    mode = models.CharField(verbose_name='扫描方式', max_length=16)
class Statisticalstatement(models.Model):
    """统计报表表(包含扫描结果的汇总信息)"""
    numbers = models.IntegerField(verbose_name='漏洞数量', max_length=8)
    distribution = models.CharField(verbose_name='严重程度分布', max_length=16)
    advice = models.CharField(verbose_name='修复建议', max_length=64)



