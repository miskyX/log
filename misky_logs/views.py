from django.shortcuts import render

from .models import Topic
from .models import Entry
from .forms import TopicForm
from .forms import EntryForm

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required #限制访问（装饰器）
from django.http import Http404


# Create your views here.
# 在这里创建视图

def index(request):
    """学习笔记的主页"""

    return render(request,'misky_logs/index.html')

@login_required
#装饰器用于下面topics函数，
#加了个@和login_required，可以让python在运行topics的代码前，先运行login_requied的代码
def topics(request):
    """显示所有的主题"""
    #topics = Topic.objects.order_by('date_added')
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request,'misky_logs/topics.html',context)


@login_required
def topic(request,topic_id):
    """显示单个主题及其条目"""
    topic = Topic.objects.get(id=topic_id)
    # 确认请求的主题属于当前用户
    if topic.owner != request.user:
        raise Http404 #给它返回异常404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request,"misky_logs/topic.html",context)


@login_required
def new_topic(request):
    """可以添加新主题"""
    if request.method != 'POST':  #未提交数据，创建一个新表单
        form = TopicForm()

    else:
        form = TopicForm(request.POST)  #提交数据，那么就要进行数据处理
        if form.is_valid(): # 验证字段是否符合要求
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save() #保存数据，写入数据库
            return HttpResponseRedirect(reverse('misky_logs:topics')) #浏览器重定向，并且刷新能看见新的主题
    context = {'form':form}
    return render(request,'misky_logs/new_topic.html',context)


@login_required
def new_entry(request,topic_id):
    """在特定主题中添加新的条目"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form  = EntryForm()

    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('misky_logs:topic',args=[topic_id]))
    context = {'topic':topic, 'form':form}
    return render(request,'misky_logs/new_entry.html',context)


@login_required
def edit_entry(request,entry_id):
    """编辑现有的条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404 #给它返回异常404

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST) #必输是POST，而不是post
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('misky_logs:topic',args=[topic.id]))
    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request,'misky_logs/edit_entry.html',context)



