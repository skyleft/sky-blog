#-*-coding:utf-8 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import RequestContext
# Create your views here.

def reg(request):
    # return HttpResponse('hello,please register.')
    return render_to_response('account/register.html',{'title':'请您注册'},context_instance=RequestContext(request))

