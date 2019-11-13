from django.conf.urls import url

from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),

    # 显示所有主题
    url(r'^topics/$', views.topics, name='topics'),

    # 显示一个主题下的所有日志
    url(r'^topic/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # 用于添加新主题的网页
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    # 用于添加新日志的网页
    url(r'^new_entry/(?P<topic_id>\d+)$', views.new_entry, name='new_entry'),

    # 用于修改日志
    url(r'^edit_entry/(?P<entry_id>\d+)$', views.edit_entry, name='edit_entry'),
]


app_name = 'learning_logs'
