# Django

### 1.安装django

```shell
pip install django
```

```
C:/python3
	-python.exe
	-Scripts
		-pip.exe
		-django-admin.exe	[工具、创建django项目中的文件和文件夹]
	-Lib
		-内置模块
		-site-package
			-openyxl
			-python-docx
			-django			[框架源码]
```

### 2.创建项目



> django 项目包含默认的文件和文件夹

#### 2.1在终端

+ 打开终端
+ 进入常用代码文件目录

+ 创建项目

```shell
django-admin startprojext mysite(文件名)
python manage.py startapp blog(app名)
```



#### 2.2 Pycharm



特殊说明

+ 命令行：创建的项目是标准的

+ pycharm:在标准的基础上增添一些东西

  + 创建了template 目录(删除)
  + setting.py中[删除]

  ```python
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [BASE_DIR / 'templates']
          ,
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
  ]
  ```

  + 将上面的改变成为下面的

  ```python
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [],
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
  ]
  ```

  默认项目文件介绍

  ```shell
  E:.
  │  manage.py					【项目的管理、启动项目、创建app、数据处理】
  └─Mysite
          asgi.py		[接收网络请求]
          settings.py	【项目配置】			【**常常操作**】
          urls.py		【URLH和函数的对应关系】【**常常操作**】
          wsgi.py		[接收网络请求]
          __init__.py
  ```

### 3 APP(application)

```
-项目
	-app.用户管理【表结构、表函数、HTTL模块、CSS】
	-app,订单管理
	-app,后端管理
	-app 网页
	-app,API
```

+ 创建项目

  + ```shell
    python manage.py startapp app1(应用名)---windows版
    ```

```tree
├─app1
│  │  admin.py			【固定，不用动】django 默认了admin后台管理
│  │  apps.py			【固定，不用动】app启动类
│  │  models.py			【**重要**】数据库变更操作		
│  │  tests.py			【固定，不用动】单元测试
│  │  views.py			【**重要**】函数
│  │  __init__.py
│  │
│  ├─migrations			【固定，不用动】数据库变更记录
│  │      __init__.py
│  │
│  └─__pycache__
│          __init__.cpython-39.pyc
│
└─Mysite
    │  asgi.py
    │  settings.py
    │  urls.py
    │  wsgi.py
    │  __init__.py
    │
    └─__pycache__
            settings.cpython-39.pyc
            __init__.cpython-39.pyc

```

### 4. 快速上手

+ 确保app已注册

![image-20221009224936395](E:\Hswing\Documents\PYTHON\Django\assets\appres.png)

+ 编写URL和视图函数之间的关系(urls.py)

![image-20221009225452022](E:\Hswing\Documents\PYTHON\Django\assets\urls_views.png)

+ 编写视图函数【views.py】

![image-20221009225705924](E:\Hswing\Documents\PYTHON\Django\assets\views.png)

+ 启动django项目

  + 命令行启动

    ```
    python manage.py runserver
    ```

  + pycharm启动

  .![image-20221009230224626](E:\Hswing\Documents\PYTHON\Django\assets\pycharm_begin.png)

#### 4.1 页面

```
-url-->函数
-函数
```

![image-20221009231313560](E:\Hswing\Documents\PYTHON\Django\assets\page_add.png)

#### 4.2 Template模板

![image-20221009233406546](E:\Hswing\Documents\PYTHON\Django\assets\templatedemo.png)

#### 4.3 静态文件

开发过程一般将：

+ amge

+ CSS

+ JS

  + 注意事项

    + 当图片无法正常显示时，需要在setting.py处进行修改

    ```python
    STATIC_URL = '/static/'
    STATICFILES_DIRS=[
        os.path.join(BASE_DIR,'static')
    ]
    ```

以上均当静态文件处理

##### 4.3.1 static 目录

![image-20221010140114820](E:\Hswing\Documents\PYTHON\Django\assets\static.png)

##### 4.3.2 引用静态文件

![image-20221010140421767](E:\Hswing\Documents\PYTHON\Django\assets\static_diaoyong.png)

### 5.模板语法

> 本质上:在HTML中写一些占位符，有数据对这些占位符进行替换和处理

![image-20221010205622011](E:\Hswing\Documents\PYTHON\Django\assets\Hdemo.png)

+ 视图函数(Views.py)的render内部

1. 读取含有模板语法的HTML文件
2. 内部进行渲染（模板语法执行并替换数据），最终得到，只包含HTML标签的字符串
3. 将渲染（替换）完成的字符串返还给用户浏览器

#### 案例：伪联通消息中心(无法爬取)

### 6.请求与想要

![image-20221012103349265](E:\Hswing\Documents\PYTHON\Django\assets\PG.png)

+ 关于重定向

![image-20221012102845613](E:\Hswing\Documents\PYTHON\Django\assets\POST_GET.png)

#### 案例：用户登录功能

![image-20221012112220531](E:\Hswing\Documents\PYTHON\Django\assets\login.png)

### 7. 数据库操作

+ MYSQL 数据库+pymysql

``` python
# 1. 连接Mysql
conn=pymysql.Connect(host="127.0.0.1",post=3306,user='root',
passwd='root123',charset='utf8',db="unicom")
curosr=conn.cursor(cursor=pymysql.cursors.DicCursor)

# 2.发送指令
curosr.execute("insert into admin (username,password,mobile) value ('www','123','151515')")
conn.commit()

# 3.关闭
curosr.close()
conn.close()
```

+ Django开发开发操作数据库更加简单，内部提供了ORM框架

![image-20221012142804855](E:\Hswing\Documents\PYTHON\Django\PIC\orm_sql.png)

#### 7.1 安装第三方模块

``` shell
pip install musqlclient
```

#### 7.2 ORM

> ORM 两大功能

+ 创建、修改、删除数据库中的表(不用写SQL语句)。【无法创建数据库】
+ 操作表中的数据不用写SQL语句)。

##### 1.创建数据库

+ 启动MYSQL
+ 自带工具创建数据库

```mysql
 create database djangoLearn DEFAULT CHARSET utf8 COLLATE utf8_general_ci
```

##### 2.django连接数据库

<font color='Red'>在settings.py文件中进行配置</font>

```python
DATABASES={
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME':'djangolearn',#数据名
        'USER':'root',#Mysql账户名
        'PASSWORD':'root',#Mysql 密码
        'HOST':'127.0.0.1',#那台机器安装了MYSQL
        'PORT':3306,#端口

    }
}

```

![image-20221012150027886](E:\Hswing\Documents\PYTHON\Django\assets\Mysql_set.png)

##### 3. django 操作表

+ 创建表
+ 删除表
+ 修改表

1.创建表：在models.py文件中：





```python
"""
create table app01_userinfo(
    id bigit auto_increment primary key,                         
    name varchar (32),
    password varchar (64),
    asc int 
)
"""

```

![image-20221012163521400](E:\Hswing\Documents\PYTHON\Django\assets\models.png)

执行命令：

```shell
 python manage.py makemigrations
 python manage.py migrate
```

![image-20221012170230646](E:\Hswing\Documents\PYTHON\Django\assets\DBINIT.png)





在表中新增列时，由于已存在列中存在数据，所以新增列必须要指定新增对应的数据.

+ 1.手动输入一个值
+ 设置默认值

```
    size=models.CharField(max_length=16 ,default='2')

```

+ 允许为空

```
    Data=models.IntegerField(null=True,blank=True)
```

以后在开发中如果想要对表结构进行调整：

+ models.py操作类即可
+ 命令

```
python manage.py makemigrations
python manage.py migrate
```

##### 4.操作表中的数据

```python
 #1.新建
    # Department.objects.create(title="销售部")
    # Department.objects.create(title="IT部")
    # Department.objects.create(title="运营部")
    # UserINfo.objects.create(name="詹x",password="123",age=12)
    # UserINfo.objects.create(name="小小",password="111",age=22)

    #2.删除
    # UserINfo.objects.filter(id=2).delete()
    # Department.objects.all().delete()
    # 3.获取数据
    #data_list=[对象，对象，对象],QuerySet类型
    # data_list=UserINfo.objects.all()
    # for obj in data_list:
    #     print(obj.id,obj.name,obj.password,obj.age)
    # print(data_list)
    # data_list=[对象，对象，对象]
    # data_list=UserINfo.objects.filter(id=1)
    #3.1 获取第一条数据【对象】
    # row_obj=UserINfo.objects.filter(id=1).first()
    # print(row_obj.id,row_obj.name,row_obj.password,row_obj.age)

   ### 4.更新数据
    # UserINfo.objects.all().update(password=999)
    UserINfo.objects.filter(name="詹x").update(age=999)
```

### 案例：

#### 1.展示用户列表

1. 创建一个url和views中的函数，并建立对应关系

![image-20221016213441644](E:\Hswing\Documents\PYTHON\Django\assets\manage1.png)

+ 函数
  + 获取用户所有信息
  + HTML渲染

#### 2.添加用户

+ url
+ 函数
  + GET ,看到页面，输入内容
  + POST，提交->写入数据库

#### 3.删除用户

+ url
+ 函数

```http
http://127.0.0.1:8000/info/delete/?nid=1
http://127.0.0.1:8000/info/delete/?nid=2
http://127.0.0.1:8000/info/delete/?nid=3
def 函数(reques):
	nid=request.GET.get("nid")
	UserInfo.objects.filter(id=nid).delete()
	return HttpResponse("删除成功")
```



# Django 开发

+ 主题;员工管理系统

## 1.创建项目

![image-20221017141648011](E:\Hswing\Documents\PYTHON\Django\assets\1.png)

## 2.创建app

```
python manage.py startapp app01(app名)
```

![image-20221017142136102](E:\Hswing\Documents\PYTHON\Django\assets\2.png)

注册app:

![image-20221017142629760](E:\Hswing\Documents\PYTHON\Django\assets\3.png)

## 3. 创建表结构(Django)

![image-20221017151557614](E:\Hswing\Documents\PYTHON\Django\assets\image-20221017151557614.png)

<table>
    <tr>
        <th>id</th>
        <th>title</th>
    </tr>
    <tr>
    	<td>2</td>
        <td>客服</td>
    </tr>
        <tr>
    	<td>3</td>
        <td>运维</td>
    </tr>

   <table>
    <tr>
        <th>id</th>
        <th>gender</th>
    </tr>
    <tr>
    	<td>1</td>
        <td>男</td>
    </tr>
        <tr>
    	<td>2</td>
        <td>女</td>
    </tr>

<table>
    <tr>
        <th>id</th>
    	<th>name</th>
    	<th>password</th>
    	<th>age</th>
    	<th>account</th>
    	<th>create_time</th>
    	<th>depart_id</th>
        <th>gender</th>
    </tr>
        <tr>
        <td>3</td>
    	<td>tt</td>
    	<td>123</td>
    	<td>18</td>
    	<td>1000</td>
    	<td>2021/11/11</td>
    	<td>3</td>
        <th>1</th>
    </tr>
        <tr>
        <td>5</td>
    	<td>xx</td>
    	<td>123</td>
    	<td>18</td>
    	<td>1000</td>
    	<td>2021/11/11</td>
    	<td>3</td>
        <th>2</th>
    </tr>
        <tr>
        <td>6</td>
    	<td>dd</td>
    	<td>123</td>
    	<td>18</td>
    	<td>1000</td>
    	<td>2021/11/11</td>
    	<td>3</td>
         <th>2</th>
    </tr>

+ 用户储存名称？ID?
  + ID 、数据库范式(理论知识)，常见开发都是这样【节省内存开销】
  + 名称、较大的公式、查询的次数比较多，连表操作比较耗时，【加速查找，允许数据冗余】
+ 部门ID只能是部门表中以存在ID
+ 部门被删除、关联的用户
  + 删除用户
  + 部门ID列置空

```python
from django.db import models

# Create your models here.
class Department(models.Model):
    """部门表"""
    # id=models.BigAutoField(verbose_name="ID",primary_key=True)
    title=models.CharField(verbose_name="标题",max_length=32)

class UserInfo(models.Model):
    """员工表"""
    name=models.CharField(verbose_name="姓名",max_length=16)
    password=models.CharField(verbose_name="密码",max_length=64)
    age=models.IntegerField(verbose_name="年龄")
    account=models.DecimalField(verbose_name="账户余额",max_length=10,decimal_places=2,default=0)
    create_time=models.DateTimeField(verbose_name="入职时间")

    #无约束
    # depart_id=models.BigIntegerField(verbose_name="部门ID")

    #1.有约束
    #   -to：标识与哪张表关联
    #   -to_field,表中那一列关联
    #2.django自动
    #   -写的depart
    #   -生成数据列 depart_id
    #3.部门表被删除
    #3.1级联删除
    # depart=models.ForeignKey(to="Department",to_field="id",on_delete=models.CASCADE)
    #3.2 置空
    # depart=models.ForeignKey(to="Department",to_field="id",null=True,blank=True,on_delete=models.SET_NULL)
```

## 4.在MYSQL 中生成表

+ 工具连接MYSQL生成数据库

```MYSQL
 create database djangoLearn DEFAULT CHARSET utf8 COLLATE utf8_general_ci
```

+ 修改配置文件 连接MySQL

```
DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME':'Employ',#数据库名
        'USER':'root',
        'PASSSWORD':'root',
        'HOST':'127.0.0.1',
        'PORT':3306
    }
}
```



![image-20221018161515222](E:\Hswing\Documents\PYTHON\Django\assets\image-20221018161515222.png)

+ django 命令生成数据库

```
python manage.py makemigrations
python manage.py migrate
```

![image-20221018162754382](E:\Hswing\Documents\PYTHON\Django\assets\image-20221018162754382.png)

+ 表结构创建成功

![image-20221018163214860](E:\Hswing\Documents\PYTHON\Django\assets\image-20221018163214860.png)

## 5.静态文件管理

![image-20221018163601438](E:\Hswing\Documents\PYTHON\Django\assets\image-20221018163601438.png)

## 6.部门管理

>体验，最原始方法
>
>Django中提供Form和ModelFrom组件(方便)

### 6.1部门列表

1. 写一个url
2. 写一个views ,连接起来

![image-20221018173109789](E:\Hswing\Documents\PYTHON\Django\assets\image-20221018173109789.png)

![image-20221018185716452](E:\Hswing\Documents\PYTHON\Django\assets\image-20221018185716452.png)

#### 6.1.1添加部门

#### ![image-20221018185800915](E:\Hswing\Documents\PYTHON\Django\assets\image-20221018185800915.png)

![image-20221018185825193](E:\Hswing\Documents\PYTHON\Django\assets\image-20221018185825193.png)

![image-20221018185915087](E:\Hswing\Documents\PYTHON\Django\assets\image-20221018185915087.png)

#### 6.1.2 删除部门信息

```python
def depart_delete(request):
    """删除部门"""
    #http://127.0.0.1:8000/depart/delete/?nid=1
    nid=request.GET.get('nid')

    models.Department.objects.filter(id=nid).delete()
    # return redirect("/depart/list/")
    return  redirect("/depart/list")
```

![image-20221018203008673](E:\Hswing\Documents\PYTHON\Django\assets\image-20221018203008673.png)

![image-20221018202936451](E:\Hswing\Documents\PYTHON\Django\assets\image-20221018202936451.png)

#### 6.1.3 修改部门信息

```python
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
```

![image-20221018203405530](E:\Hswing\Documents\PYTHON\Django\assets\image-20221018203405530.png)

![image-20221018203444841](E:\Hswing\Documents\PYTHON\Django\assets\image-20221018203444841.png)

## 7.模板的继承

+ 部门列表
+ 添加部门
+ 编辑部门



定义模板：layout.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    {% block css %}{% endblock%}
</head>
<body>
<h1>标题</h1>
<div>
    {% block content %}{% endblock %}
</div>
<h1>底部</h1>
        <script src="{% static 'js/jquery-3.5.1.min.js' %}"></script>
{% block js %}{% endblock%}
    </body>

</html>
```

继承模板

```html
{% extends 'layout.html' %}

{% block css %}
<link rel="stylesheet" href="{% static 'pluxx.css'%}"
      <style>
.....		
</style>
{% endblock%}




{% block content %}
	<h1>首页</h1>

{% endblock %}

{% block js %}
<link rel="stylesheet" href="{% static 'jquery-3.5.1.min.js '%}"
      <style>
.....		
</style>
{% endblock%}
```

## 8. 用户管理

```sql
insert into app01_userinfo(name,password,age,account,create_time,gender,depart_id)
values("刘东","123",23,100.68,"2010-11-11",1,1);

insert into app01_userinfo(name,password,age,account,create_time,gender,depart_id)
values("王强","1243",23,101.68,"2010-11-11",1,5);

insert into app01_userinfo(name,password,age,account,create_time,gender,depart_id)
values("朱虎飞","999",33,9900.68,"2021-11-11",1,1);
```

```
+-------------+---------------+------+-----+---------+----------------+
| Field       | Type          | Null | Key | Default | Extra          |
+-------------+---------------+------+-----+---------+----------------+
| id          | bigint(20)    | NO   | PRI | NULL    | auto_increment |
| name        | varchar(16)   | NO   |     | NULL    |                |
| password    | varchar(64)   | NO   |     | NULL    |                |
| age         | int(11)       | NO   |     | NULL    |                |
| account     | decimal(10,2) | NO   |     | NULL    |                |
| create_time | datetime(6)   | NO   |     | NULL    |                |
| gender      | smallint(6)   | NO   |     | NULL    |                |
| depart_id   | bigint(20)    | NO   | MUL | NULL    |                |
+-------------+---------------+------+-----+---------+----------------+
```

![image-20221019160450792](E:\Hswing\Documents\PYTHON\Django\assets\image-20221019160450792.png)

### 8.1新建用户

+ 原始方式思路：不会采用(本质)【麻烦】

```
--用户提交的信息，没有数据校验
--错误，页面应该有错误提示
--页面上，每一个字段都需要我们重新写一篇
--关联数据，需要手动去获取，并循环展示到页面上
```



+ django组件
  + From组件（小简便）+代码
  + ModelFrom组件(最简便)

### 8.1.1初识别From

#### 1.views.py

```python
class MyFrom (From--Django内置)：
	user=from.CharField(widget=form.Input)
	pwd=form.CharFiled(widget=form.Input)
    email=form.CharFiled(widget=form.Input)
	create_time=form.CharFiled(widget=form.Input)
	depart=form.CharFiled(widget=form.Input)

def user_add(request):
    """添加用户"""
    if request.method=='GET':
        form =MyFrom()
        return render(request, "user_add.html", {"form":form})

```

#### 2.user_add.py

```html
<form method="post">   
    {{form.user}}
    {{form.pwd}}
    -----------------
    {% for field in forms%}
    	{{field }}
    {% endfor%}
<input type="text" class="form-control" placeholder="姓名" name="user">
<input type="text" class="form-control" placeholder="姓名" name="user">
<input type="text" class="form-control" placeholder="姓名" name="user">

</form>
```

### 8.1.2 ModelForm

#### 0.models.py

```python
from django.db import models

# Create your models here.
class Department(models.Model):
    """部门表"""
    # id=models.BigAutoField(verbose_name="ID",primary_key=True)
    title=models.CharField(verbose_name="标题",max_length=32)

class UserInfo(models.Model):
    """员工表"""
    name=models.CharField(verbose_name="姓名",max_length=16)
    password=models.CharField(verbose_name="密码",max_length=64)
    age=models.IntegerField(verbose_name="年龄")
    account=models.DecimalField(verbose_name="账户余额",max_digits=10,decimal_places=2,default=0)
    create_time=models.DateTimeField(verbose_name="入职时间")

    #无约束
    # depart_id=models.BigIntegerField(verbose_name="部门ID")

    #1.有约束
    #   -to：标识与哪张表关联
    #   -to_field,表中那一列关联
    #2.django自动
    #   -写的depart
    #   -生成数据列 depart_id
    #3.部门表被删除
    #3.1级联删除
    depart=models.ForeignKey(to="Department",to_field="id",on_delete=models.CASCADE)
    #3.2 置空
    # depart=models.ForeignKey(to="Department",to_field="id",null=True,blank=True,on_delete=models.SET_NULL)

    gender_choice={
        (1,"男"),
        (2,'女'),
    }
    gender=models.SmallIntegerField(verbose_name="性别",choices=gender_choice)
```



#### 1.views.py

```python
class MyFrom (ModelForm)：
	class Meta:
        model=UserInfo
        field=["name","password","age"]

def user_add(request):
    """添加用户"""
    if request.method=='GET':
        form =MyFrom()
        return render(request, "user_add.html", {"form":form})
```

#### 2.user_add.py

```python
<form method="post">   
    {{form.user}}
    {{form.pwd}}
    -----------------
    {% for field in forms%}
    	{{field }}
    {% endfor%}
<input type="text" class="form-control" placeholder="姓名" name="user">
<input type="text" class="form-control" placeholder="姓名" name="user">
<input type="text" class="form-control" placeholder="姓名" name="user">

</form>
```

##### 实例

###### views.py

```python
from django import forms
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
```

###### HTML

```HTML
{% extends 'layout.html' %}
{% block content %}
    <div>
        <div class="container">
            <div class="panel panel-default">
                <div class="panel-heading">
                    <h3 class="panel-title">新增用户</h3>
                </div>
                <div class="panel-body">
                    <form method="post" novalidate>
                        {% csrf_token %}
                        {% for field in form %}
                            <div class="form-group">
                            <label> {{ field.label }}</label>
                            {{ field }}
                                <span style="color: red">{{ field.errors.0}}</span>

                            </div>

                        {% endfor %}
                        <button type="submit" class="btn btn-primary">提 交</button>
                    </form>
                </div>
                </form>
            </div>
        </div>
    </div>
{% endblock %}

```

+ 部门管理

+ 用户管理

  + 用户列表

  + 新建用户

    ```sql
    --ModelFROM,针对数据库中的某个表
    -From
    ```

    

### 8.3编辑用户

+ 点击编辑，跳转到编辑页面(将编辑行的ID传输过去)
+ 编辑页面(默认数据，根据ID去获取)

+ 提交：

  + 错误提示

  + 数据校验

  + 在数据库更新

  + ```sql
    modelS.UserInfo.fliter(id=4).update(..)
    ```

```
views.py
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
        form.save()#数据库更新
        return redirect("/user/list")
    return render(request, "user_edit.html", {'form': form})

```

### 8.4删除用户

```py
def user_delete(request,nid):
    """删除用户"""
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list")

```

## 9.靓号管理

### 9.1表结构

<table>
    <tr>
    	<th>id</th>
        <th>mobile</th>
        <th>price</th>
        <th>level(级别类似于性别)</th>
        <th>statue（1 未占用/2 已占用）</th>
    </tr>
</table>

+ 根据表结构的需求，在models.py创建类(由类生成数据库中的表)

```python
class   PrettyNumber(models.Model):
    """靓号表"""
    mobile=models.CharField(verbose_name="手机号" ,max_length=11)
    price= models.IntegerField(verbose_name="价格",default=99999)
    level_choice=(
        (1,"一星"),
        (2, "二星"),
        (3, "三星"),
        (4,"四星"),
        (5, "五星"),

)
    level=models.SmallIntegerField(verbose_name="级别",choices=level_choice,default=1)
    status_choice=(
        (1, "已占用"),
        (2, '未占用'),
    )
    status=models.SmallIntegerField(verbose_name="级别",choices=status_choice,default=2)
```

+ 模拟创建数据

```
insert into app01_prettynumber(mobile,price,level,status)values("111111111",19,1,2);
```

### 9.2 靓号列表

+ url

+ 函数

  + 获得所有账号
  + 结合render+html 将靓号罗列出来

  ```
  id 号码 价格 级别（中文） 状态（中文）
  ```

  ```python
  def prettynum_list(request):
      #select *from 表 order by level desc;
      query_set=models.PrettyNumber.objects.all().order_by("-level")
      return render(request,"PrettyNum_list.html",{"queryset":query_set})
  ```

  

### 9.3 新建靓号

+ 列表点击跳转页面

+ url

+ 函数

  + 实例化类的对象
  + 通过render将对象传入HTML中
  + 模板的循环展示所有字符

+ ModelForm类(含号码验证)

```
from django.core.validators import RegexValidator
from django.core.validators import ValidationError
class   PrettyModelForm(forms.ModelForm):
    #方式一
    mobile=forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$',"手机号码格式错误")]#正则表达式
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
    # def clean_mobile(self):
    #     txt_mobile=self.cleaned_data["mobile"]
    #     if len(txt_mobile)!=11:
    #         #验证不通过
    #         raise ValidationError("格式错误")
    #     #验证通过，用户输入值
    #     return txt_mobile
```



```
Views.py
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
```

![image-20221021144756836](E:\Hswing\Documents\PYTHON\Django\assets\image-20221021144756836.png)

### 9.4 编辑靓号

+ 列表页面：prettynum/数字/edit/

+ url

+ 函数

  + 根据ID获取当前的编辑对象
  + ModelForm配合，默认显示数据
  + 提交进行修改

+ 不允许手机号重复

  + 添加：【正则表达式】【手机号不能存在】

    ```
    querset=models.PrettyNum.objects.filter(mobile='13329913540')
    #第二种：
    #True/False
    exists=models.PrettyNumber.objects.filter(mobile='13329913540').exists()
    
    ```

    + 编辑：【正则表达式】

    ```python
    排除自己意外，其他数据是否手机号码重复
    #id!=2 abd mobile='13329913540'
    exists=models.PrettyNumber.objects.filter(mobile='13329913540').exclude(id=2))
    
    ```

    ### 

### 9.5搜索手机号

```python
models.PrettyNum.objects.filter(mobile='13329913540',id=12)

data_dict={"mobile":"13329913540","id"=123}
models.PrettyNum.objects.filter(**data_dict)
```

```python
models.PrettyNum.objects.filter(id=12) #等于12
models.PrettyNum.objects.filter(id_gt=12) #大于
models.PrettyNum.objects.filter(id_gte=12) #大于
models.PrettyNum.objects.filter(id=12) #等于12
models.PrettyNum.objects.filter(id_lt=12)#小于12
models.PrettyNum.objects.filter(id_lte=12) #小于等于12
```

```python
##字符串(筛选)

#等于999
models.PrettyNumber.objects.filter(mobile="999")

##以1817开头   models.PrettyNumber.objects.filter(mobile__startswith="1817")

##以9952结尾      models.PrettyNumber.objects.filter(mobile__endwith="9952")

##包含999
1.
models.PrettyNumber.objects.filter(mobile__contains="999")
2.
data_dict=dta_dict={mobile__contains="999"}
models.PrettyNum.objects.filter(**data_dict)

```

+ PrettyNum_list.html代码的调整

+ ![image-20221022132556708](E:\Hswing\Documents\PYTHON\Django\assets\image-20221022132556708.png)

```html
        <div style="margin-bottom: 10px" class="clearfix">
            <a class="btn btn-success" href="/prettynum/add/">
                <span class="glyphicon glyphicon-plus-sign" aria-hidden="true"></span>
                新增靓号
            </a>
            <div style="float: right ;width: 300px">
                <form method="get">
                    <div class="input-group">
                        <input type="text" name="q" class="form-control" placeholder="Search for..." value={{ search_data }}>
                        <span class="input-group-btn">
                        <button class="btn btn-default" type="submit">
                            <span class="glyphicon glyphicon-search" aria-hidden="true"></span>
                        </button>
                        </span>
                    </div>
                </form>

                </div>

        </div>
```

+ views.py

```python
def prettynum_list(request):
    """靓号列表"""
    data_dict={}
    search_data=request.GET.get('q',"")
    if search_data:
        data_dict['mobile__contains']=search_data
    # q=models.PrettyNumber.objects.filter(mobile__startswith="18171799952",id=3)
    #select *from 表 order by level desc;
    query_set=models.PrettyNumber.objects.filter(**data_dict).order_by("-level")
    return render(request,"PrettyNum_list.html",{"queryset":query_set,"search_data":search_data})

```

###  9.6分页管理

```python
 queryse=models.PrettyNum.object.all() 
 query_set=models.PrettyNumber.objects.filter(id=1)[0:10]

 #第1页  
 query_set=models.PrettyNumber.objects.all()[0:10]

 #第2页  
 query_set=models.PrettyNumber.objects.all()[10:20]

 #第3页  
 query_set=models.PrettyNumber.objects.all()[20:30]
# 数据量
 table_count=models.PrettyNumber.objects.all().count()

```

+ 分页逻辑与规则

#  Django开发的额外知识

# django 连接 已有数据库

1. ```python
   首先在settiing文件中配置对应数据库的内容
   DATABASES = {
       "default": {
           "ENGINE": "django.db.backends.mysql",
           'NAME': 'bookdb',  # 数据库名
           'USER': 'root',#账户
           'PASSWORD': 'root',#密码
           'HOST': '127.0.0.1',
           'PORT': 3306
       }
   }
   ```

2. ```python
   在setting.py的同级文件中init.py加入
   import pymysql
   pymysql.install_as_MySQLdb()
   ```

3. ```python
   在控制台输入python manage.py inspectdb > models.py
   就可以将需要的数据库导入
   ```

4. ```python
   #读取已有数据库的数据
   import pymysql
   pymysql.install_as_MySQLdb()
   ```

5. ```python
   当选择使用的表单的时候进行下属操作
   #当使用石将managed转换为true
       class Meta:
           managed = True
           db_table = 'tb_book'
   ```

[(2条消息) django如何连接Mysql中已有的数据库_ChangYan.的博客-CSDN博客_django连接已有数据库](https://blog.csdn.net/changyana/article/details/122790568)
