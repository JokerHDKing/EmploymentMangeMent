from django.db import models

# Create your models here.
class Department(models.Model):
    """部门表"""
    # id=models.BigAutoyyField(verbose_name="ID",primary_key=True)
    title=models.CharField(verbose_name="标题",max_length=32)
    def __str__(self):
        return self.title

class UserInfo(models.Model):
    """员工表"""
    name=models.CharField(verbose_name="姓名",max_length=16)
    password=models.CharField(verbose_name="密码",max_length=64)
    age=models.IntegerField(verbose_name="年龄")
    account=models.DecimalField(verbose_name="账户余额",max_digits=10,decimal_places=2,default=0)
    create_time=models.DateField(verbose_name="入职时间")

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
    depart=models.ForeignKey(verbose_name="部门",to="Department",to_field="id",on_delete=models.CASCADE)
    #3.2 置空
    # depart=models.ForeignKey(to="Department",to_field="id",null=True,blank=True,on_delete=models.SET_NULL)

    gender_choice={
        (1,"男"),
        (2,'女'),
    }
    gender=models.SmallIntegerField(verbose_name="性别",choices=gender_choice)

class   PrettyNumber(models.Model):
    """靓号表"""
    mobile=models.CharField(verbose_name="手机号" ,max_length=11,unique=True)
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
