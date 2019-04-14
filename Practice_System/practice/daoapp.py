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

def getResource(role_id):
    '''
    根据角色id查询此角色可访问的资源列表
    :param role_id:
    :return: list
    '''
    commonresource = ['/practice/login/', '/practice/', '/practice/logout/', '/practice/index/']

