from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from datetime import datetime
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 50)
    def __str__ (self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length = 25)
    def __str__(self):
        return self.name


class Blog(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    category = models.ForeignKey(Category , on_delete = models.CASCADE)
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length = 75 , verbose_name= 'Blog Title' )
    slug = models.SlugField(max_length=250, null=True, blank=True)
    desc = models.TextField()
    image = models.ImageField(upload_to = 'blogimg', blank = True , default='')

    created_at = models.DateTimeField(default=datetime.now)
    update_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)
        

class Comment(models.Model):
    blog = models.ForeignKey(Blog , on_delete = models.CASCADE, related_name="blogcomment")
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    blog_comment = models.CharField(max_length = 150)
    
    def __str__(self):
        return self.blog_comment


class SubComment(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    commnet = models.ForeignKey(Comment, on_delete = models.CASCADE, related_name='subcomment')
    content = models.CharField(max_length = 150)

    def __str__(self):
        return self.content



