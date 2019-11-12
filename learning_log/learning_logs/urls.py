from django.conf.urls import url

from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),

    # 显示所有主题
    url(r'^topics/$', views.topics, name='topics'),

    # 显示一个主题下的所有日志
    url(r'^topic/(?P<topic_id>\d+)/$', views.topic, name='topic')
]


app_name = 'learning_logs'
