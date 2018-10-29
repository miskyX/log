
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
    path('topics/(?P<topic_id>\d+)/',views.topic,name='topic')
]