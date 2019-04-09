from django.db import models


# 角色表
class Role(models.Model):
    # 角色id
    role_id = models.IntegerField(primary_key=True, blank=False)
    # 角色名
    role_name = models.CharField(max_length=10, blank=False)
    # 在admin管理app中显示的名称
    def __str__(self):
        return '{}:{}'.format(self.role_id, self.role_name)


# 菜单表
class Menu(models.Model):
    # 菜单id
    menu_id = models.IntegerField(primary_key=True, blank=False)
    # 角色id
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    # 菜单名
    menu_name = models.CharField(max_length=4)
    # 父菜单id
    parent_id = models.IntegerField(default=0)
    # 在admin管理app中显示的名称
    def __str__(self):
        return '{}:{}'.format(self.menu_id, self.menu_name)

# 教师表
class Teacher(models.Model):
    # 教职工号
    tea_id = models.IntegerField(primary_key=True, blank=False)
    # 登陆密码
    tea_pwd = models.CharField(max_length=20)
    # 姓名
    tea_name = models.CharField(max_length=10)
    # 联系号码
    tea_phone = models.CharField(max_length=11)
    # 邮箱
    tea_email = models.CharField(max_length=15)
    # 所在学院
    college = models.CharField(max_length=20)
    # 教师岗位
    tea_post = models.CharField(max_length=20)
    # 在admin管理app中显示的名称
    def __str__(self):
        return '{}:{}'.format(self.tea_id,self.tea_name)

# 学生表
class Student(models.Model):
    # 学号
    stu_id = models.IntegerField(primary_key=True, blank=False)
    tea_id = models.ForeignKey(Teacher,  on_delete=models.CASCADE)
    # 登陆密码
    stu_pwd = models.CharField(max_length=20)
    # 姓名
    stu_name = models.CharField(max_length=10)
    # 年龄
    stu_age = models.IntegerField(default=0)
    # 联系号码
    phone_num = models.CharField(max_length=11)
    # 邮箱
    e_mail = models.CharField(max_length=15)
    # 专业
    major = models.CharField(max_length=20)
    # 年级
    grade = models.IntegerField(default=0)
    # 班级
    stu_class = models.CharField(max_length=10)
    # 居住地址
    address = models.CharField(max_length=40)
    # 政治面貌
    political_status = models.CharField(max_length=10)
    # 目标岗位
    target_post = models.CharField(max_length=20)
    # 意向就业地
    intention_area = models.CharField(max_length=40)
    # 简历
    resume = models.FileField(upload_to='practice/resume/')
    # 三方协议
    tripartite_agreement = models.BooleanField(default=False)
    # 企业实习协议
    practice_agreement = models.BooleanField(default=False)
    # 就业协议
    employment_agreement = models.BooleanField(default=False)
    # 教师打分
    tea_mark = models.IntegerField(default=0)
    # 企业打分
    ent_mark = models.IntegerField(default=0)
    # 在admin管理app中显示的名称
    def __str__(self):
        return '{}:{}'.format(self.stu_id,self.stu_name)

# 企业表
class Enterprise(models.Model):
    # 企业id
    ent_id = models.IntegerField(primary_key=True, blank=False)
    # 登陆密码
    ent_pwd = models.CharField(max_length=20)
    # 企业名字
    ent_name = models.CharField(max_length=40)
    # 企业简介
    introduction = models.CharField(max_length=150)
    # 企业所在地区
    ent_address = models.CharField(max_length=40)
    # 联系号码
    ent_phone = models.CharField(max_length=11)
    # 企业邮箱
    ent_email = models.CharField(max_length=15)
    # 企业招聘负责人
    principal = models.CharField(max_length=10)
    # 在admin管理app中显示的名称
    def __str__(self):
        return '{}:{}'.format(self.ent_id,self.ent_name)

# 岗位表
class Job(models.Model):
    # 岗位id
    job_id = models.IntegerField(primary_key=True)
    # 企业id
    ent_id = models.ForeignKey(Enterprise,  on_delete=models.CASCADE)
    # 岗位名
    job_name = models.CharField(max_length=20)
    # 岗位职责描述
    job_desc = models.CharField(max_length=100)
    # 招聘人数
    employ_num = models.IntegerField(default=0)
    # 薪资
    salary = models.IntegerField(default=0)
    # 工作时间
    job_time = models.IntegerField(default=0)
    # 在admin管理app中显示的名称
    def __str__(self):
        return '{}:{}'.format(self.job_id,self.job_name)

# 选择表
class Choice(models.Model):
    choice_id = models.IntegerField(primary_key=True)
    job_id = models.ForeignKey(Job,  on_delete=models.CASCADE)
    stu_id = models.ForeignKey(Student,  on_delete=models.CASCADE)
    result = models.CharField(max_length=10)
    # 在admin管理app中显示的名称
    def __str__(self):
        return '{}:{}'.format(self.choice_id, self.stu_id)

# 实习周记表
class WeekRecord(models.Model):
    weekRecord_id = models.IntegerField(primary_key=True)
    stu_id = models.ForeignKey(Student,  on_delete=models.CASCADE)
    recordContent = models.CharField(max_length=2048)
    # 在admin管理app中显示的名称
    def __str__(self):
        return '{}:{}'.format(self.weekRecord_id,self.stu_id)
