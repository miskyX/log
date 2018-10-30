
'''定义misky_logs的URL模式'''

from django.urls import path

from . import views

app_name = 'misky_logs'

urlpatterns = [
    #主页
    path('',views.index, name='index'),

    #显示所有主题
    path('topics/',views.topics, name="topics"),

    # 添加特定主题的详细页面
    path('topics/(?P<topic_id>\d+)/',views.topic,name='topic'),

    #添加新主题的网页
    path('new_topic/',views.new_topic,name='new_topic'),

    #添加用于新条目的网页
    path('new_entry/(?P<topic_id>\d+)/',views.new_entry,name='new_entry'),

    #添加用于编辑条目的页面
    path('edit_entry/(?P<entry_id>\d+)/',views.edit_entry, name='edit_entry'),
]