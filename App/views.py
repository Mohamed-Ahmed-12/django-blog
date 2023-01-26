from django.shortcuts import render
from .models import Blog, Category, Tag ,Comment
from .forms import BlogForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(
        request, "index.html", {"blogs": blogs, "cate": categories, "tags": tags}
    )


def blog(request, slug):
    return render(request, "blog.html", {"blog": Blog.objects.get(slug=slug)})


def search(request):
    txt = request.GET.get("searchtxt")
    return render(
        request, "index.html", {"blogs": Blog.objects.filter(title__icontains=txt)}
    )


def display_by_category(request, cate):
    return render(
        request,
        "index.html",
        {"blogs": Blog.objects.filter(category=Category.objects.get(name__exact=cate))},
    )


def display_by_tag(request, tag):
    return render(
        request,
        "index.html",
        {"blogs": Blog.objects.filter(tags=Tag.objects.get(name__exact=tag))},
    )


def create_blog(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = BlogForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.instance.user = request.user
            form.save()
            return HttpResponseRedirect("/index/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BlogForm()
    return render(request, "createblog.html", {"blogform": form})

def add_comment(request,slug):
    comment = request.POST.get('comment')
    userID = int(request.POST.get('userid'))
    blogID = int(request.POST.get('blogid'))
    user = User.objects.get(id=userID)
    if Blog.objects.filter(id=blogID).exists:
        blog = Blog.objects.get(id=blogID)
        Comment.objects.create(blog= blog, user=user ,blog_comment=comment ).save()

    return HttpResponseRedirect(redirect_to=f"/blog/{blog.slug}")