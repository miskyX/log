from django.contrib import admin

# Register your models here.
# 在这里注册你的模型
# 我们现在这里注册Topic模型

from misky_logs.models import Topic
from misky_logs.models import Entry

admin.site.register(Topic) #使用自带命令注册我们的topic模型

admin.site.register(Entry)