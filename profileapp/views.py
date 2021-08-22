from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    #template_name = 'profileapp/create.html'