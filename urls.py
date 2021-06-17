from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('blog_list/', views.blog_list),
    path('U_brain/', views.U_brain, name = "blog-post"),
    path('It_companies/', views.It_companies),
    path('javascript/', views.javascript_framework),
]