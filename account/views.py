#-*-coding:utf-8 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
# Create your views here.

author_group = Group.objects.get_by_natural_key("author");
def reg(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		username = email.split('@')[0]
		user = User.objects.create_user(username=username,password=password,email=email)
		user.is_staff = True
		user.groups.add(author_group)
		user.save()
		user = authenticate(username=username, password=password)
		#登陆用户
		login(request,user)
		#return render_to_response('account/register_done.html',{'title':'注册成功'},context_instance=RequestContext(request))
		#注册成功，跳转到完善资料页面
		return redirect(reverse('account.views.complete_profile',args=[]))

	elif request.method == 'GET':
		return render_to_response('account/register.html',{'title':'请您注册'},context_instance=RequestContext(request))
	
@login_required
def complete_profile(request):
	user = request.user
	return render_to_response('account/complete_profile.html',{
		'user':user,
		'title':'请完善个人资料'
		},context_instance=RequestContext(request))
