# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User, Permission
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
  return render(request, 'admin/index.html')

def users(request):
  userlist = User.objects.all()
  return JsonResponse(userlist)
