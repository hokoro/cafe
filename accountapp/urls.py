from django.contrib.auth.views import LoginView
from django.urls import path, reverse

from accountapp.views import main_page, AccountCreateView, AccountDetailView

app_name = 'accountapp'

urlpatterns =[
    path('main_page/',main_page,name = 'main_page'),
    path('create/',AccountCreateView.as_view(),name = 'create'),
    path('login/',LoginView.as_view(template_name='accountapp/login.html'),name = 'login'),
    path('detail/<int:pk>',AccountDetailView.as_view(),name='detail')
]