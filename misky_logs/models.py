from django.db import models

# Create your models here.

#导入了模块models，让我们开始创建模型，模型就是我们学习的类

class Topic(models.Model):
    """用户学习的主题"""
    #我们定义了一个topic的类，它继承了MODEL的属性

    text = models.CharField(max_length=200)  #定义一个text属性，字符或文本，限制了长度（名称，城市等等）
    date_added = models.DateTimeField(auto_now_add=True) #定义一个添加日期，继承了属性，自动设置成当前时间

    def __str__(self):
        '''返回模型字符串表示'''
        return self.text #返回上面text的内容

class Entry(models.Model):
    """学到有关某个主题的知识"""

    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    #topic是一个外键的实例，引用数据库中的一条记录
    text = models.TextField()
    #text是一个TEXTFIELD的实例。
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

        #嵌套了一个meta类，用于储存管理模型的额外信息
    def __str__(self):
        """返回模型字符串表示"""
        return self.text[:50] + "..."
