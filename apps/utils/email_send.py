#coding:utf-8
__author__ = 'neo'
__date__ = ' 下午 3:48'
from users.models import EmailVerifyReord
from random import Random
from django.core.mail import send_mail
from mxonline.settings import EAMIL_FROM


def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars)-1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0,length)]
    return str


def send_register_email(email,send_type='register'):
    email_record = EmailVerifyReord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.sendtype = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type ==  'register':
        email_title = '暮雪在线网注册激活链接'
        email_body = "请点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{0}".format(code)
        send_status=send_mail(email_title,email_body,EAMIL_FROM,[email])
        if send_status:
            pass