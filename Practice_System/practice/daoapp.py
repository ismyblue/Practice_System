from practice.models import *

def getMenu(role_id):
    '''
    通过role_id获取此角色所有菜单
    :param role_id:
    :return: menu
    menu = {
        '企业信息': {
            '信息查看': 'enterprise/review/',
            '信息修改': 'enterprise/update/',
        },
        '招聘管理': {
            '岗位公开': 'enterprise/review/',
            '审核简历': 'enterprise/update/',
            '岗位公开1': 'enterprise/review/',
            '审核简历2': 'enterprise/update/',
        },
        '实习生考核': {
            '实习生': 'enterprise/review/',
            '实习生记录': 'enterprise/update/',
            '嘻嘻嘻': 'enterprise/review/',
            '哈哈哈': 'enterprise/update/',
        },
    }
    '''
    role_id = int(role_id)
    # 某角色的所有菜单项
    datas = Menu.objects.filter(role_id = role_id)
    # 父菜单
    parentMenu = {}
    # 要返回的菜单字典
    menu = {}
    for m in datas:
        if m.parent_id == 0:
            parentMenu[m.menu_id] = m.menu_name
            menu[m.menu_name] = {}
            menu[m.menu_name][m.menu_name] = m.url_name
    for m in datas:
        if m.parent_id != 0:
            pmenuname = parentMenu[m.parent_id]
            if pmenuname in menu[pmenuname].keys():
                del menu[pmenuname][pmenuname]
            menu[pmenuname][m.menu_name] = m.url_name
    return menu


def getUsername(role_id, user_id):
    '''
    根据role_id,user_id，返回此账号的名称
    :param role_id: 角色id
    :param user_id: 登陆账号
    :return: str
    '''
    username = ''
    if not isinstance(role_id, int) or not isinstance(user_id, int):
        return None
    if role_id == 2:    #如果是老师
        username = Teacher.objects.get(tea_id=user_id).tea_name
    elif role_id == 3:  #如果是企业
        username = Enterprise.objects.get(ent_id=user_id).ent_name
    elif role_id == 4:  #如果是学生
        username = Student.objects.get(stu_id=user_id).stu_name
    return username


def getInformations(role_id, user_id):
    '''
    根据role_id, user_id获取用户的信息
    :param role_id: 角色id
    :param user_id: 账号id
    :return: dict informations
    '''
    # infoNames = {'tea_id': '用户名', 'tea_name': '姓名', 'tea_phone': '联系方式', 'tea_email': '邮箱', 'college': '学校',
    #              'tea_post': '课程', 'ent_id': '用户名', 'ent_name': '公司名称', 'introduction': '公司介绍',
    #              'ent_address': '公司地址', 'ent_phone': '联系方式', 'ent_email': '邮箱', 'principal': '资本',
    #              'stu_id': '用户名', 'stu_name': '姓名', 'stu_age': '年龄', 'phone_num': '联系方式', 'e_mail': '邮箱',
    #              'major': '专业', 'grade': '年级', 'political_status': '政治面貌', 'target_post': '目标岗位',
    #              'intention_area': '意向地区', 'resume': '简历', 'tripartite_agreement': '三方协议',
    #              'practice_agreement': '实习协议', 'employment_agreement': '劳动合同', 'tea_mark': '老师评分',
    #              'ent_mark': '企业评分'}
    informations = {}
    if not isinstance(role_id, int) or not isinstance(user_id, int):
        return None
    if role_id == 2:
        teacher = Teacher.objects.get(tea_id=user_id)
        informations = __getTeacherInformations(teacher)
    elif role_id == 3:
        enterprise = Enterprise.objects.get(ent_id=user_id)
        informations = __getEnterpriseInformations(enterprise)
    elif role_id == 4:
        student = Student.objects.get(stu_id=user_id)
        informations = __getStudentInformations(student)
    return informations


def getProfile(role_id, user_id):
    '''
    根据role_id, user_id获取用户的信息Profile
    :param role_id: 角色id
    :param user_id: 用户id
    :return: dict
    profile = {'tea_id': '123', 'tea_name': '黄老师', 'tea_phone': '1395640024323', 'tea_email': 'i12@123.com'}
    '''
    profile = {}
    if not isinstance(role_id, int) or not isinstance(user_id, int):
        return None
    if role_id == 2:
        teacher = Teacher.objects.get(tea_id=user_id)
        profile = __getTeacherProfile(teacher)
    elif role_id == 3:
        enterprise = Enterprise.objects.get(ent_id=user_id)
        profile = __getEnterpriseProfile(enterprise)
    elif role_id == 4:
        student = Student.objects.get(stu_id=user_id)
        profile = __getStudentProfile(student)
    return profile


def __getStudentInformations(student):
    '''
    获取学生账号信息
    :param student:
    :return:
    '''
    informations = {}
    informations['学号'] = student.stu_id
    informations['姓名'] = student.stu_name
    informations['年龄'] = student.stu_age
    informations['联系方式'] = student.phone_num
    informations['邮箱'] = student.e_mail
    informations['专业'] = student.major
    informations['年级'] = student.grade
    informations['班级'] = student.stu_class
    informations['地址'] = student.address
    informations['政治面貌'] = student.political_status
    informations['指导老师'] = student.tea_id.tea_name
    informations['目标岗位'] = student.target_post
    informations['意向地区'] = student.intention_area
    informations['简历'] = student.resume.url
    informations['三方协议'] = student.tripartite_agreement
    informations['实习协议'] = student.practice_agreement
    informations['劳动合同'] = student.employment_agreement
    informations['老师评分'] = student.tea_mark
    informations['企业评分'] = student.ent_mark
    return informations


def __getTeacherInformations(teacher):
    '''
    获取教师账号信息
    :param teacher:
    :return: dict
    '''
    informations = {}
    informations['用户名'] = teacher.tea_id
    informations['姓名'] = teacher.tea_name
    informations['联系方式'] = teacher.tea_phone
    informations['邮箱'] = teacher.tea_email
    informations['学院'] = teacher.college
    informations['职位'] = teacher.tea_post
    return informations


def __getEnterpriseInformations(enterprise):
    '''
    获取企业账号信息
    :param enterprise:
    :return: dict
    '''
    informations = {}
    informations['用户名'] = enterprise.ent_id
    informations['公司名称'] = enterprise.ent_name
    informations['公司介绍'] = enterprise.introduction
    informations['公司地址'] = enterprise.ent_address
    informations['联系方式'] = enterprise.ent_phone
    informations['邮箱'] = enterprise.ent_email
    informations['负责人'] = enterprise.principal
    return informations


def __getStudentProfile(student):
    '''
    获取学生账号信息
    :param student:
    :return: dict profile
    '''
    profile = {}
    profile['stu_id'] = student.stu_id
    profile['stu_name'] = student.stu_name
    profile['stu_age'] = student.stu_age
    profile['phone_num'] = student.phone_num
    profile['e_mail'] = student.e_mail
    profile['major'] = student.major
    profile['grade'] = student.grade
    profile['stu_class'] = student.stu_class
    profile['address'] = student.address
    profile['political_status'] = student.political_status
    profile['target_post'] = student.target_post
    profile['intention_area'] = student.intention_area
    profile['resume'] = student.resume.url
    profile['tripartite_agreement'] = student.tripartite_agreement
    profile['practice_agreement'] = student.practice_agreement
    profile['employment_agreement'] = student.employment_agreement
    return profile


def __getTeacherProfile(teacher):
    '''
    获取教师账号信息
    :param teacher:
    :return: dict
    '''
    profile = {}
    profile['tea_id'] = teacher.tea_id
    profile['tea_name'] = teacher.tea_name
    profile['tea_phone'] = teacher.tea_phone
    profile['tea_email'] = teacher.tea_email
    profile['college'] = teacher.college
    profile['tea_post'] = teacher.tea_post
    return profile


def __getEnterpriseProfile(enterprise):
    '''
    获取企业账号信息
    :param enterprise:
    :return: dict
    '''
    profile = {}
    profile['ent_id'] = enterprise.ent_id
    profile['ent_name'] = enterprise.ent_name
    profile['introduction'] = enterprise.introduction
    profile['ent_address'] = enterprise.ent_address
    profile['ent_phone'] = enterprise.ent_phone
    profile['ent_email'] = enterprise.ent_email
    profile['principal'] = enterprise.principal
    return profile


def getResource(role_id):
    '''
    根据角色id查询此角色可访问的资源列表
    :param role_id:
    :return: list
    '''
    commonresource = ['/admin/', '/practice/', '/practice/login/', '/practice/logout/', '/practice/index/']

