from . import views
from django.urls import path
urlpatterns = [
    path('index/',views.index , name='index'),
    path('search',views.search , name='search'),
    path('create/',views.create_blog , name='create_blog'),
    path('blog/<slug:slug>',views.blog , name='blog'),
    path('blog/category/<str:cate>', views.display_by_category , name='by_category'),
    path('blog/tag/<str:tag>', views.display_by_tag , name='by_tag'),
    path('blog/<slug:slug>/addcomment', views.add_comment , name='add_comment'),
]