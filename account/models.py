#--*-- coding:utf-8 -*-

from django.db import models

# Create your models here.
import datetime,logging
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings as _settings

log = logging.getLogger('accuont.models')

class ProfileBase(type):
    def __new__(cls, name, bases, attrs): 
        module = attrs.pop('__module__')

        parents = [b for b in bases if isinstance(b, ProfileBase)]

        if parents:
            fields = []
            for obj_name, obj in attrs.items():   
                if isinstance(obj, models.Field): fields.append(obj_name)   
                User.add_to_class(obj_name, obj)
        return super(ProfileBase, cls).__new__(cls, name, bases, attrs)   
class ProfileUser(object):
    __metaclass__ = ProfileBase
    
class MyProfile(ProfileUser):
    real_name = models.CharField(max_length = 30,blank=True) 
    nick_name = models.CharField(max_length = 30,blank=True)  
    sex = models.IntegerField(default = 1)                
    portrait = models.CharField(max_length=200, default='/media/images/default.png')       