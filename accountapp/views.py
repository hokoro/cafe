from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView


def main_page(request):
    return HttpResponse('Hello World')


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm  # user 형식 계정

    template_name = 'accountapp/create.html'
    success_url = reverse_lazy('accountapp:main_page')
