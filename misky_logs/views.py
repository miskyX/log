from django.shortcuts import render

from .models import Topic

# Create your views here.
# 在这里创建视图

def index(request):
    """学习笔记的主页"""

    return render(request,'misky_logs/index.html')


def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request,'misky_logs/topics.html',context)

def topic(request,topic_id):
    """显示单个主题及其条目"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request,"misky_logs/topic.html",context)