# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateUserForm


def index(request):
    form = CreateUserForm()
    context = {'form':form}
    return render(request, 'accounts/index.html', context)
   