#coding:utf-8
__author__ = 'neo'
__date__ = ' 下午 2:24'

import xadmin
from .models import EmailVerifyReord,Banner
from xadmin import views

class BaseSeting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = '后台管理系统'
    site_footer = '谢谢'
    menu_style = 'accordion'



class EmailVerifyReordAdmin(object):
    list_display = ['code','email','sendtype','sendtime']
    search_fields = ['code','email','sendtype']
    list_filter = ['code','email','sendtype','sendtime']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index','add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index','add_time']



xadmin.site.register(EmailVerifyReord,EmailVerifyReordAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSeting)
xadmin.site.register(views.CommAdminView,GlobalSettings)