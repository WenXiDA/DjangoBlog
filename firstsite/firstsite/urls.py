"""firstsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firstapp import views
from firstapp.coreweb import ResponseHandler
#这里可以做一个类，实现__callable__()方法，来检验是否登录或者参数是否合理，则调用如下
#path(r'test', ValidClass(views.test),name="test"),
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'blogs', ResponseHandler(views.blogs), name="blogs"),
    path(r'regist', ResponseHandler(views.regist), name = "regist"),
    path(r'login', ResponseHandler(views.login),name = "login"),
    path(r'logout', ResponseHandler(views.logout),name="logout"),
    path(r'blog/<str:name>', ResponseHandler(views.blog),name="blog"),
    path(r'myblogs', ResponseHandler(views.myblogs),name="myblogs"),
    path(r'myblog/<str:name>', ResponseHandler(views.myblog),name="myblog"),
    path(r'myblog/edit/<str:blog_name>', ResponseHandler(views.myblog_edit),name="myblog_edit"),
    path(r'edit_blog', ResponseHandler(views.myblog_edit),name="edit_blog"),
    path(r'myblog/del/<str:name>', ResponseHandler(views.myblog_del),name="myblog_del"),
    path(r'test', ResponseHandler(views.test),name="test"),
]
