from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=300)

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=300)
    alias = models.SlugField()
    create_date = models.DateField('create_date')

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    alias = models.SlugField()

    def __unicode__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length=300)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)
    content = models.TextField()
    pub_date = models.DateField('pub_date')

    def __unicode__(self):
        return self.name

class Comment(models.Model):
    author = models.CharField(max_length=100)
    postref = models.ForeignKey(Post)
    content = models.TextField()
    comment_date = models.DateField('comment_date')

    def __unicode__(self):
        return self.author
