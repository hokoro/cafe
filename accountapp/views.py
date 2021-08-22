from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView


@login_required(login_url=reverse_lazy('accountapp:login'))
def main_page(request):

    date = request.user.date_joined
    username = request.user.username

    return render(request,'accountapp/main_page.html',context={'date':date,'username':username})

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm  # user 형식 계정

    template_name = 'accountapp/create.html'

    def get_success_url(self):
        return reverse('accountapp:main_page', kwargs={'pk': self.object.pk})


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'
