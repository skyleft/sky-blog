#-*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
class Blog(models.Model):
    name = models.CharField(max_length=300)
    user = models.ForeignKey(User)
    create_date = models.DateField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "博客"
        verbose_name_plural = "博客管理"

class Category(models.Model):
    name = models.CharField(max_length=300)
    alias = models.SlugField()
    create_date = models.DateField('create_date')

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = "分类"
        verbose_name_plural = "分类管理"

class Tag(models.Model):
    name = models.CharField(max_length=100)
    alias = models.SlugField()

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = "标签"
        verbose_name_plural = "标签管理"

class Post(models.Model):
    name = models.CharField(max_length=300)
    blog = models.ForeignKey(Blog)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)
    content = models.TextField()
    score = models.IntegerField(default=0)
    pub_date = models.DateField('pub_date')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章管理"

class Comment(models.Model):
    author = models.CharField(max_length=100)
    postref = models.ForeignKey(Post)
    content = models.TextField()
    comment_date = models.DateField('comment_date')

    def __unicode__(self):
        return self.author

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = "评论管理"
