from django.shortcuts import render
from app01 import models
# def user_add(request):
#      """添加用户"""
#      name = request.POST.get("name")
#      password = request.POST.get("password")
#      age = request.POST.get("age")
#      phone = request.POST.get("phone")
#      models.UserInfo.objects.create(name=name, password=password, age=age, phone=phone)
from django import forms
class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", "phone"]
def user_model_form_add(request):
    """添加用户（ModelForm版本）"""
    form = UserModelForm()



def user_delete(request, nid):
    """删除用户"""
    models.UserInfo.objects.filter(id=nid).delete()
def user_edit(request, nid):
    """修改用户"""
    name = request.POST.get("name")
    password = request.POST.get("password")
    age = request.POST.get("age")
    phone = request.POST.get("phone")
    models.UserInfo.objects.filter(id=nid).update(name=name, password=password, age=age, phone=phone)

def user_list(request):
    """用户列表"""
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["name__contains"] = search_data
    #按照用户名查询
    models.UserInfo.objects.filter(**data_dict).order_by("+id")
    if search_data:
        data_dict["id__contains"] = search_data
    #按照id查询
    models.UserInfo.objects.filter(**data_dict).order_by("+id")


def classification_add(request):
    """添加分类信息"""
    name = request.POST.get("name")
    description = request.POST.get("description")
    models.Classification.objects.create(name=name, description=description)
def classification_delete(request, nid):
    """删除分类信息"""
    models.Classification.objects.filter(id=nid).delete()
def classification_edit(request, nid):
    """修改文章分类信息"""
    name = request.POST.get("name")
    description = request.POST.get("description")
    models.Classification.objects.filter(id=nid).update(name=name, description=description)
def classification_list(request):
    """分类信息列表"""
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["name__contains"] = search_data
    #按照分类名称查询
    models.Classification.objects.filter(**data_dict).order_by("+id")



def page_add(request):
    """添加页面信息"""
    title = request.POST.get("title")
    content = request.POST.get("content")
    models.Page.objects.create(title=title, content=content)
def page_delete(request, nid):
    """删除页面信息"""
    models.Page.objects.filter(id=nid).delete()
def page_edit(request, nid):
    """修改页面信息"""
    title = request.POST.get("title")
    content = request.POST.get("content")
    models.Page.objects.filter(id=nid).update(title=title, content=content)
def page_list(request):
    """页面信息列表"""
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["title__contains"] = search_data
    #按照页面标题查询
    models.Page.objects.filter(**data_dict).order_by("+id")




def journal_add(request):
    """添加日志信息"""
    type = request.POST.get("type")
    content = request.POST.get("content")
    time = request.POST.get("time")
    models.Journal.objects.create(type=type, content=content, time=time)
def journal_delete(request, nid):
    """删除日志信息"""
    models.Journal.objects.filter(id=nid).delete()
def journal_edit(request, nid):
    """修改日志信息"""
    type = request.POST.get("type")
    content = request.POST.get("content")
    time = request.POST.get("time")
    models.Journal.objects.filter(id=nid).update(type=type, content=content, time=time)
def journal_list(request):
    """日志列表"""
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["type__contains"] = search_data
    #按照日志类型查询
    models.Journal.objects.filter(**data_dict).order_by("+id")
    if search_data:
        data_dict["time__contains"] = search_data
    #按照日志时间查询
    models.Journal.objects.filter(**data_dict).order_by("+id")




def record_add(request):
    """添加访问信息"""
    ip = request.POST.get("ip")
    time = request.POST.get("time")
    models.Record.objects.create(ip=ip, time=time)
def record_delete(request, nid):
    """删除访问信息"""
    models.Record.objects.filter(id=nid).delete()
def record_edit(request, nid):
    """修改访问信息"""
    ip = request.POST.get("ip")
    time = request.POST.get("time")
    models.Record.objects.filter(id=nid).update(ip=ip, time=time)
def record_list(request):
    """访问列表"""
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["ip__contains"] = search_data
    #按照IP地址查询
    models.Record.objects.filter(**data_dict).order_by("+id")
    if search_data:
        data_dict["time__contains"] = search_data
    #按照访问时间查询
    models.Record.objects.filter(**data_dict).order_by("+id")



def bug_add(request):
    """添加漏洞列表信息"""
    type = request.POST.get("type")
    grade = request.POST.get("grade")
    cve = request.POST.get("cve")
    edition = request.POST.get("edition")
    models.Bug.objects.create(type=type, grade=grade, cve=cve,edition=edition)
def bug_delete(request, nid):
    """删除漏洞列表信息"""
    models.Bug.objects.filter(id=nid).delete()
def bug_edit(request, nid):
    """修改漏洞列表信息"""
    type = request.POST.get("type")
    grade = request.POST.get("grade")
    cve = request.POST.get("cve")
    edition = request.POST.get("edition")
    models.Bug.objects.filter(id=nid).update(type=type, grade=grade, cve=cve,edition=edition)
def bug_list(request):
    """漏洞列表"""
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["type__contains"] = search_data
    #按照漏洞类型查询
    models.Bug.objects.filter(**data_dict).order_by("+id")
    if search_data:
        data_dict["cve__contains"] = search_data
    #按照CVE编号查询
    models.Bug.objects.filter(**data_dict).order_by("+id")




def target_add(request):
    """添加目标列表信息"""
    ip = request.POST.get("ip")
    domain = request.POST.get("domain")
    port = request.POST.get("port")
    models.Target.objects.create(ip=ip, domain=domain, port=port)
def target_delete(request, nid):
    """删除目标列表信息"""
    models.Target.objects.filter(id=nid).delete()
def target_edit(request, nid):
    """修改目标列表信息"""
    ip = request.POST.get("ip")
    domain = request.POST.get("domain")
    port = request.POST.get("port")
    models.Target.objects.filter(id=nid).update(ip=ip, domain=domain, port=port)
def target_list(request):
    """目标列表"""
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["ip__contains"] = search_data
    #按照IP查询
    models.Target.objects.filter(**data_dict).order_by("+id")



def scanningresult_add(request):
    """添加扫描结果信息"""
    name = request.POST.get("name")
    description = request.POST.get("description")
    advice = request.POST.get("advice")
    models.Scanningresult.objects.create(name=name, description=description, advice=advice)
def scanningresult_delete(request, nid):
    """删除扫描结果信息"""
    models.Scanningresult.objects.filter(id=nid).delete()
def scanningresult_edit(request, nid):
    """修改扫描结果信息"""
    name = request.POST.get("name")
    description = request.POST.get("description")
    advice = request.POST.get("advice")
    models.Scanningresult.objects.filter(id=nid).update(name=name, description=description, advice=advice)
def scanningresult_list(request):
    """扫描结果列表"""
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["name__contains"] = search_data
    #按照漏洞名称查询
    models.Scanningresult.objects.filter(**data_dict).order_by("+id")




def scanningjournal_add(request):
    """添加扫描日志信息"""
    operation = request.POST.get("operation")
    errormessage = request.POST.get("errormessage")
    warningmessage = request.POST.get("warningmessage")
    models.Scanningjournal.objects.create(operation=operation, errormessage=errormessage, warningmessage=warningmessage)
def scanningjournal_delete(request, nid):
    """删除扫描日志信息"""
    models.Scanningjournal.objects.filter(id=nid).delete()
def scanningjournal_edit(request, nid):
    """修改扫描日志信息"""
    operation = request.POST.get("operation")
    errormessage = request.POST.get("errormessage")
    warningmessage = request.POST.get("warningmessage")
    models.Scanningjournal.objects.filter(id=nid).update(operation=operation, errormessage=errormessage, warningmessage=warningmessage)
def scanningjournal_list(request):
    """扫描日志列表"""
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["operation__contains"] = search_data
    #按照扫描过程中的操作查询
    models.Scanningjournal.objects.filter(**data_dict).order_by("+id")



def operatingrecord_add(request):
    """添加操作记录信息"""
    personnel = request.POST.get("personnel")
    time = request.POST.get("time")
    mode = request.POST.get("mode")
    models.Operatingrecord.objects.create(personnel=personnel, time=time, mode=mode)
def operatingrecord_delete(request, nid):
    """删除操作记录信息"""
    models.Operatingrecord.objects.filter(id=nid).delete()
def operatingrecord_edit(request, nid):
    """修改操作记录信息"""
    personnel = request.POST.get("personnel")
    time = request.POST.get("time")
    mode = request.POST.get("mode")
    models.Operatingrecord.objects.filter(id=nid).update(personnel=personnel, time=time, mode=mode)
def operatingrecord_list(request):
    """操作记录列表"""
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["personnel__contains"] = search_data
    #按照扫描人员查询
    models.Operatingrecord.objects.filter(**data_dict).order_by("+id")
    if search_data:
        data_dict["time__contains"] = search_data
    #按照扫描时间查询
    models.Operatingrecord.objects.filter(**data_dict).order_by("+id")



def statisticalstatement_add(request):
    """添加统计报表信息"""
    numbers = request.POST.get("numbers")
    distribution = request.POST.get("distribution")
    advice = request.POST.get("advice")
    models.Statisticalstatement.objects.create(numbers=numbers, distribution=distribution, advice=advice)
def Statisticalstatement_delete(request, nid):
    """删除统计报表信息"""
    models.Statisticalstatement.objects.filter(id=nid).delete()
def Statisticalstatement_edit(request, nid):
    """修改统计报表信息"""
    numbers = request.POST.get("numbers")
    distribution = request.POST.get("distribution")
    advice = request.POST.get("advice")
    models.Statisticalstatement.objects.filter(id=nid).update(numbers=numbers, distribution=distribution, advice=advice)
def Statisticalstatement_list(request):
    """统计报表列表"""
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["numbers__contains"] = search_data
    #按照漏洞数量查询
    models.Statisticalstatement.objects.filter(**data_dict).order_by("+id")
    if search_data:
        data_dict["distribution__contains"] = search_data
    #按照严重程度分布查询
    models.Statisticalstatement.objects.filter(**data_dict).order_by("+id")

def add(request):
    return render(request, "add.html")