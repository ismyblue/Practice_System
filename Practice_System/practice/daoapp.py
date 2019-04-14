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


def getProfile(role_id, user_id):
    '''
    根据role_id, user_id获取用户的信息
    :param role_id: 角色id
    :param user_id: 账号id
    :return: dict
    '''
    # infoNames = {'tea_id': '用户名', 'tea_name': '姓名', 'tea_phone': '联系方式', 'tea_email': '邮箱', 'college': '学校',
    #              'tea_post': '课程', 'ent_id': '用户名', 'ent_name': '公司名称', 'introduction': '公司介绍',
    #              'ent_address': '公司地址', 'ent_phone': '联系方式', 'ent_email': '邮箱', 'principal': '资本',
    #              'stu_id': '用户名', 'stu_name': '姓名', 'stu_age': '年龄', 'phone_num': '联系方式', 'e_mail': '邮箱',
    #              'major': '专业', 'grade': '年级', 'political_status': '政治面貌', 'target_post': '目标岗位',
    #              'intention_area': '意向地区', 'resume': '简历', 'tripartite_agreement': '三方协议',
    #              'practice_agreement': '实习协议', 'employment_agreement': '劳动合同', 'tea_mark': '老师评分',
    #              'ent_mark': '企业评分'}
    profile = {}
    print(role_id, user_id)
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


def __getStudentProfile(student):
    '''
    获取学生账号信息
    :param student:
    :return:
    '''
    profile = {}
    profile['学号'] = student.stu_id
    profile['姓名'] = student.stu_name
    profile['年龄'] = student.stu_age
    profile['联系方式'] = student.phone_num
    profile['邮箱'] = student.e_mail
    profile['专业'] = student.major
    profile['年级'] = student.grade
    profile['政治面貌'] = student.political_status
    profile['指导老师'] = student.tea_id.tea_name
    profile['目标岗位'] = student.target_post
    profile['意向地区'] = student.intention_area
    profile['简历'] = student.resume.url
    profile['三方协议'] = student.tripartite_agreement
    profile['实习协议'] = student.practice_agreement
    profile['劳动合同'] = student.employment_agreement
    profile['老师评分'] = student.tea_mark
    profile['企业评分'] = student.ent_mark
    return profile


def __getTeacherProfile(teacher):
    '''
    获取教师账号信息
    :param teacher:
    :return: dict
    '''
    print(teacher)
    profile = {}
    profile['用户名'] = teacher.tea_id
    profile['姓名'] = teacher.tea_name
    profile['联系方式'] = teacher.tea_phone
    profile['邮箱'] = teacher.tea_email
    profile['学院'] = teacher.college
    profile['职位'] = teacher.tea_post
    return profile


def __getEnterpriseProfile(enterprise):
    '''
    获取企业账号信息
    :param enterprise:
    :return: dict
    '''
    profile = {}
    print(enterprise)
    profile['用户名'] = enterprise.ent_id
    profile['公司名称'] = enterprise.ent_name
    profile['公司介绍'] = enterprise.introduction
    profile['公司地址'] = enterprise.ent_address
    profile['联系方式'] = enterprise.ent_phone
    profile['邮箱'] = enterprise.ent_email
    profile['负责人'] = enterprise.principal
    return profile


def getResource(role_id):
    '''
    根据角色id查询此角色可访问的资源列表
    :param role_id:
    :return: list
    '''
    commonresource = ['/admin/', '/practice/', '/practice/login/', '/practice/logout/', '/practice/index/']

