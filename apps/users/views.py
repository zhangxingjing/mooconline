from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
# Create your views here.
from apps.users.models import UserProfile
from django.views.generic.base import View
from apps.users.forms import LoginForm,RegisterForm
from django.contrib.auth.hashers import make_password
from apps.utils.email_send import send_register_email
from apps.organization.models import CityDict,CourseOrg,Teacher
from apps.operation.models import Course

class LoginView(View):
    def get(self,request):
        # course = Course()
        # course.org = CourseOrg.objects.get(id=1)
        # course.name = 'django从入门到放弃'
        # course.desc = '教你如何成为大牛'
        # course.detail = '不错的课程'
        # course.degree = 'cj'
        # course.image = '/media/courses/2016/11/mysql.jpg'
        # course.save()
        # t = Teacher()
        # org = CourseOrg()
        # t.org = CourseOrg.objects.get(id=4)
        # t.name = 'Andy'
        # t.work_years = 4
        # t.work_company = '腾讯公司'
        # t.work_position = '架构师'
        # t.point = '负责'
        # t.save()
        # city = CityDict()
        # city.name = '天津市'
        # city.desc = city.name
        # city.save()
        # org = CourseOrg()
        # org.name = '慕课网6'
        # org.desc = '慕课网6'
        # org.address = '北京市海淀区中关村北大街'
        # org.city = CityDict.objects.get(id=6)
        # org.save()
        return render(request, 'login.html', {})

    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request,'login.html',{'message': '用户名或密码错误'})
        else:
            return render(request, 'login.html', {'login_form':login_form})



class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

#
# def userlogin(request):
#     if request.method == 'POST':
#         user_name = request.POST.get('username','')
#         pass_word = request.POST.get('password','')
#         user = authenticate(username=user_name,password=pass_word)
#         if user is not None:
#             login(request,user)
#             return render(request,'index.html')
#         else:
#             return render(request,'login.html',{'message':'用户名或密码错误'})
#     elif request.method == 'GET':
#         return render(request,'login.html',{})


class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm()
        return render(request,'register.html',{'register_form':register_form})
    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email')
            pass_word = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(pass_word)
            user_profile.save()
            # send_register_email(user_name,'register')
            return render(request,'login.html')
        else:
            return render(request,'register.html',{'register_form':register_form,})


class CourseList(View):
    def get(self,request):
        return render(request,'course-list.html')


class TeacherList(View):
        def get(self, request):
            return render(request,'teachers-list.html')

