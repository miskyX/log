
"""为应用程序users定义URL模式"""

from django.urls import path
from django.contrib.auth.views import LoginView

from . import views
app_name = 'users'

#LoginView.template_name = 'users/login.html'

urlpatterns = [
    #path('login/',LoginView.as_view(),name ='login'),
    path('logout/',views.logout_view, name = 'logout')   ,
    path('login/',LoginView.as_view(template_name='users/login.html'),name='login'),
    path('register/',views.register, name ='register'),
]
