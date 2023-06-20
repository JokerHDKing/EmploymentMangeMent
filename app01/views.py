from django.shortcuts import render,redirect,HttpResponse
from app01 import  models
from django.core.validators import RegexValidator
from django.core.validators import ValidationError
from django import forms
from django.utils.safestring import mark_safe
# Create your views here.
def depaet_list(request):
    """部门列表"""

    # 前往数据库中获取所有部门列表
    #querysert类型
    #[对象，对象，对象]
    title=models.Department.objects.all()
    return render(request,'depart_list.html',{'title':title})

def depart_add(request):
    """添加部门"""
    if request.method=="GET":
        return render(request,"depart_add.html")
    #获取用户POST提交过来的数据(title输入为空)
    title=request.POST.get("title")

    #保存到数据库
    models.Department.objects.create(title=title)
    #重定向为部门列表
    return  redirect("/depart/list")

def depart_delete(request):
    """删除部门"""
    #http://127.0.0.1:8000/depart/delete/?nid=1
    nid=request.GET.get('nid')

    models.Department.objects.filter(id=nid).delete()
    # return redirect("/depart/list/")
    return  redirect("/depart/list")

def depart_edit(request,nid):
    # http://127.0.0.1:8000/depart/4/edit
    #根据nid,获取他的数据[obj,]
    if request.method=="GET":
        row_object=models.Department.objects.filter(id=nid).first()
        print(row_object.id,row_object.title)
        return render(request, "depart_edit.html", {"row_object": row_object})
    title=request.POST.get("title")
    # 根据ID 找到数据库中的数据进行更新
    #当有多个时
    # models.Department.objects.filter(id=nid).update(title=title,code="xx")
    models.Department.objects.filter(id=nid).update(title=title)
    #重定向返回部门列表
    return  redirect("/depart/list")

def user_list(request):
    query_set=models.UserInfo.objects.all()

    # for obj in query_set:
    #     print(obj.id,obj.name,obj.account,obj.create_time.strftime("%Y-%m-%d-%H-%M"))
    #     print(obj.get_gender_display())
    #     # obj.depart      根据id自动去关联的标中获取哪一行数据depart对象
    #     # obj.depart_id   获取数据库中存储的那个字段值
    return render(request,'user_list.html',{"queryset":query_set})

def user_add(request):
    """添加用户"""
    if request.method=='GET':
        context={
            "gender_choices":models.UserInfo.gender_choice,
            "depart_list":models.Department.objects.all()
        }
        return render(request, "user_add.html", context)
    #获取用户读取的数据

    user=request.POST.get('user')
    pwd=request.POST.get('pwd')
    age=request.POST.get('age')
    account=request.POST.get('ac')
    ctime=request.POST.get('ctime')
    gender=request.POST.get('gender')
    depart_id=request.POST.get('dp')

    #添加到数据库
    models.UserInfo.objects.create(name=user,password=pwd,age=age,
                                   account=account,create_time=ctime,
                                   gender=gender,depart_id=depart_id)
    # 返回用户页面
    return redirect("/user/list")

#########################ModelFrom实例###################################

class UserModelForm(forms.ModelForm):
    name = forms.CharField(min_length=3, label="用户名")

    # password=forms.CharField(min_length=3,label="用户名",validators=)

    class Meta:

        model=models.UserInfo
        fields=["name","password","age","account","create_time",
                "gender","depart"]
        # widgets={
        #     "name":forms.TextInput(attrs={"class":"form-control"})
        # }
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #循环找到所有插件，添加"class":"form-control"
        for name ,field in self.fields.items():
            print(name,field)
            field.widget.attrs={"class":"form-control","placeholder":field.label}
def user_model_form_add(request):
    """添加用户(ModelFrom版本)"""
    if request.method == 'GET':
        form=UserModelForm()
        return render(request, 'user_model_form_add.html', {"form": form})

    #用户POST提交数据，数据校验
    form =UserModelForm(data=request.POST)
    if form.is_valid():
        #如果数据合法，保存到数据库中
        # {'name': '吴娅莉', 'password': '666666', 'age': 12, 'account': Decimal('0'),
        #  'create_time': datetime.datetime(2001, 12, 15, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')), 'gender': 2,
        #  'depart': < Department: 媒体企划部 >}
        # print(form.cleaned_data)
        # models.UserInfo.objects.create(..)
        form.save()
        return redirect("/user/list")
    #校3验失败
    # print(form.errors)
    return render(request,'user_model_form_add.html',{"form":form})

def user_edit(request,nid):
    """编辑用户"""
    #根据ID去获取数据需要编辑哪一行数据
    # nid = request.GET.get('nid')
    row_object = models.UserInfo.objects.filter(id=nid).first()

    if request.method=="GET":
        form=UserModelForm(instance=row_object)
        return render(request ,"user_edit.html",{'form':form})
    form = UserModelForm(data=request.POST,instance=row_object)
    if form.is_valid():#数据校验
        #默认保存用户输入的数据，如果想要再用户输入以外增加一点值
        # from.instance.字段名=值；
        form.save()
        return redirect("/user/list")
    return render(request, "user_edit.html", {'form': form})

def user_delete(request,nid):
    """删除用户"""
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list")
######################靓号管理#############################
# from models  import PrettyNumber
def prettynum_list(request):

    """靓号列表"""
    data_dict={}
    search_data=request.GET.get('q',"")
    if search_data:
        data_dict['mobile__contains']=search_data
    # q=models.PrettyNumber.objects.filter(mobile__startswith="18171799952",id=3)
    #select *from 表 order by level desc;
    #1.根据用户想要访问的页码，计算出起止位置
    page=int(request.GET.get('page',1))
    page_size=15#每页显示15条数据
    start=(page-1)*page_size
    end=page*page_size


    query_set=models.PrettyNumber.objects.filter(**data_dict).order_by("-level")[start:end]

    # 数据总条数
    table_count = models.PrettyNumber.objects.all().count()

    #总页码
    total_page_count,div=divmod(table_count,page_size)
    if div:
        total_page_count+=1
    # 页码
    #计算出，显示当前页的前5页、后5页
    plus=5
    if total_page_count<=2*plus:
        #数据库种的数据比较少
        start_page=1
        end_page=10
    else:
        # 数据库种的数据比较多
        if page<=plus:
            start_page=1
            end_page=2*plus
        else:
            #当前页大于5
            #当前+5>大于总页码
            if page+5>total_page_count:
                start_page=total_page_count-2*plus
                end_page=total_page_count
            else:
                start_page=page-plus
                end_page=page+plus


    """
    <li><a href="/prettynum/list/?page=1">1</a></li>
    <li><a href="/prettynum/list/?page=2">2</a></li>
    <li><a href="/prettynum/list/?page=3">3</a></li>
    <li><a href="/prettynum/list/?page=4">4</a></li>
    <li><a href="/prettynum/list/?page=5">5</a></li>
    """
    page_str_list=[]
    #首页
    page_str_list.append('<li><a href="?page={}">首页</a></li>'.format(1))
    # 上一页
    if page > 1:
        prev = '<li><a href="?page={}">上一页</a></li>'.format(page - 1)
        page_str_list.append(prev)
    #页面
    for i in range(start_page,end_page+1):
        if i ==page:
            ele='<li class="active"><a href="?page={}">{}</a></li>'.format(i,i)
        else:
            ele='<li><a href="?page={}">{}</a></li>'.format(i,i)

        page_str_list.append(ele)

    #下一页
    if page<=total_page_count:
        nexv = '<li><a href="?page={}">下一页</a></li>'.format(page + 1)
        page_str_list.append(nexv)

    #尾页
    page_str_list.append('<li><a href="?page={}">尾页</a></li>'.format(total_page_count))
    page_string=mark_safe("".join(page_str_list))

    return render(request,"PrettyNum_list.html",{"queryset":query_set,"search_data":search_data,"page_string":page_string})

class   PrettyModelForm(forms.ModelForm):
    #方式一
    mobile=forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$',"手机号码格式错误")]
    )
    class Meta:
        model = models.PrettyNumber
        fields = ["mobile", "price", "level", "status"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环找到所有插件，添加"class":"form-control"
        for name, field in self.fields.items():
            # print(name, field)
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}
    #验证：方式二
    def clean_mobile(self):
        txt_mobile=self.cleaned_data["mobile"]
        #当前编辑一行的ID
        #pirnt(self.instance.pk)
        #第二种：
        exists=models.PrettyNumber.objects.filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError("手机号已存在")
        if len(txt_mobile)!=11:
            #验证不通过
            raise ValidationError("格式错误")
        #验证通过，用户输入值
        return txt_mobile

def prettynum_add(request):
    """添加用户(ModelFrom版本)"""
    if request.method == 'GET':
        form=PrettyModelForm()
        return render(request, 'prettyNum_add.html', {"form": form})

    #用户POST提交数据，数据校验
    form =PrettyModelForm(data=request.POST)
    if form.is_valid():
        #如果数据合法，保存到数据库中
        # {'name': '吴娅莉', 'password': '666666', 'age': 12, 'account': Decimal('0'),
        #  'create_time': datetime.datetime(2001, 12, 15, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')), 'gender': 2,
        #  'depart': < Department: 媒体企划部 >}
        # print(form.cleaned_data)
        # models.UserInfo.objects.create(..)
        form.save()
        return redirect("/prettynum/list")
    #校3验失败
    # print(form.errors)
    return render(request,'prettyNum_add.html',{"form":form})

class   PrettyEditModelForm(forms.ModelForm):
    mobile=forms.CharField(disabled=True,label="手机号")

    class Meta:
        model = models.PrettyNumber
        fields = ['mobile', "price", "level", "status"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环找到所有插件，添加"class":"form-control"
        for name, field in self.fields.items():
            # print(name, field)
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}
    #验证：方式二
    # def clean_mobile(self):
    #     txt_mobile=self.cleaned_data["mobile"]
    #     if len(txt_mobile)!=11:
    #         #验证不通过
    #         raise ValidationError("格式错误")
    #     #验证通过，用户输入值
    #     return txt_mobile
def prettynum_edit(request,nid):
    #通过id获取那一行数据
    row_object = models.PrettyNumber.objects.filter(id=nid).first()
    if request.method=="GET":
        form=PrettyEditModelForm(instance=row_object)
        return render(request ,"prettynum_edit.html",{'form':form})
    form = PrettyEditModelForm(data=request.POST,instance=row_object)
    if form.is_valid():#数据校验
        #默认保存用户输入的数据，如果想要再用户输入以外增加一点值
        # from.instance.字段名=值；
        form.save()
        return redirect("/prettynum/list")
    return render(request,'prettynum_edit.html',{'form':form})

def prettynum_delete(request,nid):
    """删除靓号"""
    models.PrettyNumber.objects.filter(id=nid).delete()
    return redirect("/prettynum/list")