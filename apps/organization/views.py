from django.shortcuts import render
from django.views.generic.base import View
from apps.organization.models import CourseOrg,CityDict
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from apps.operation.forms import UserAskForm
from django.http import HttpResponse
# Create your views here.


class OrgList(View):
    def get(self, request):
        org = CourseOrg.objects.all()
        hot_orgs = org.order_by('click_num')[:3]
        city = CityDict.objects.all()

        #城市筛选
        city_id = request.GET.get('city','')
        if city_id:
            org = org.filter(city_id=int(city_id))
        #类别筛选
        category = request.GET.get('ct', '')
        if category:
            org = org.filter(category=category)
        org_num = org.count()
        #排名筛选
        sort = request.GET.get('sort','')
        if sort:
            org = org.order_by(sort)
        #分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(org, 5, request=request)
        orgs = p.page(page)
        return render(request,'org-list.html',{
            'org':orgs,
            'city':city,
            'org_num':org_num,
            'city_id':city_id,
            'category':category,
            'hot_orgs':hot_orgs,
            'sort':sort,
        })


class UserAskView(View):
    '''
    用户添加咨询
    '''
    def post(self,request):
        user_ask = UserAskForm(request.POST)
        if user_ask.is_valid():
            user_ask1 = user_ask.save(commit=True)
            return HttpResponse("{'status':'success'}",content_type='application/json')
        else:
            return HttpResponse("添加出错")


class DetailHomepageView(View):
    def get(self,request):
        return render(request,'org-detail-homepage.html')


class DetailTeacherView(View):
    def get(self,request):
        return render(request,'org-detail-teachers.html')


class DetailDescView(View):
    def get(self, request):
        return render(request, 'org-detail-desc.html')


class DetailCourseView(View):
    def get(self, request):
        return render(request, 'org-detail-course.html')