from django.shortcuts import render_to_response
from models import Blog,Post,Category,Tag,Comment
from django.shortcuts import get_object_or_404
from django.template import RequestContext
import time
from exceptions import Exception

def index(request):
    #blog = Blog.objects.all()[0]
    #categorys = Category.objects.all()
    #posts = Post.objects.all()
    return render_to_response('main/main.html',{},context_instance=RequestContext(request))

def category(request,category_id_tmp):
    blog = Blog.objects.all()[0]
    categorys = Category.objects.all()
    cate = get_object_or_404(Category,pk=category_id_tmp)
    posts = Post.objects.filter(category_id=category_id_tmp)
    return render_to_response('blog/archive.html',{'blog':blog,'posts':posts,'categorys':categorys,'cate':cate})

def post(request,post_id):
    blog = Blog.objects.all()[0]
    categorys = Category.objects.all()
    comments = Comment.objects.filter(postref=post_id)
    p = get_object_or_404(Post,pk=post_id)
    return render_to_response('blog/single.html',{'blog':blog,'post':p,'categorys':categorys,'comments':comments},context_instance=RequestContext(request))

def comment(request):
    try:
        au = request.POST['author']
        content = request.POST['content']
        postref_id = request.POST['post_id']
    except Exception,e:
        return render_to_response('blog/error.html',{'error':e})
    comment_date = time.strftime('%Y-%m-%d',time.localtime())
    if(postref_id and au and content):
        Comment(author=au,content=content,postref_id=postref_id,comment_date=comment_date).save()
    blog = Blog.objects.all()[0]
    categorys = Category.objects.all()
    comments = Comment.objects.filter(postref=postref_id)
    p = get_object_or_404(Post,pk=postref_id)
    return render_to_response('blog/single.html',{'blog':blog,'post':p,'categorys':categorys,'comments':comments},context_instance=RequestContext(request))
