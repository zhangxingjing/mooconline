from apps.users.models import EmailVerifyRecord
import os
from django.core.mail import send_mail
# from MoocOnline.settings import DEFAULT_FROM_EMAIL
from random import Random


def random_str(randomlength=8):
    str = ''
    chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0,length)]
    return str


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    if send_type == 'register':
        email_title = '注册激活'
        email_body = '点击链接激活:http://127.0.0.1:8000/active/{0}'.format(code)

        # send_status = send_mail(email_title,email_body,DEFAULT_FROM_EMAIL,[email])
        # if send_status:
        #     pass
