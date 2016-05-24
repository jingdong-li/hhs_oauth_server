#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _
#from django.contrib import messages

def authenticated_home(request):

    if request.user.is_authenticated():
        print("user:", request.user.is_authenticated)
        name = _("Authenticated Home")
        #this is a GET
        context= {'name':name,
              }
        template = 'authenticated-home.html'
    else:
        name = ("home")
        context = {'name': name}
        template = 'index.html'
    return render(request,template , context)

    
