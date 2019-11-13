from django.conf.urls import url
from django.contrib.auth.views import LoginView

from .views import LogoutView, register


app_name = 'users'

urlpatterns = [
    # 登录页面
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'),
        name='login'),

    # 退出登录
    url(r'^logout/$', LogoutView, name='logout'),

    # 注册
    url(r'^register/$', register, name='register')
]
