from django.contrib.auth.views import LoginView
from django.urls import path

from accountapp.views import main_page, AccountCreateView

app_name = 'accountapp'

urlpatterns =[
    path('main_page/',main_page,name = 'main_page'),
    path('create/',AccountCreateView.as_view(),name = 'create'),
    path('login/',LoginView.as_view(template_name='accountapp/login.html'),name = 'login'),
]