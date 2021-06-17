from django.shortcuts import render
from .forms import Email_Form
# Create your views here.

def index(request):
    username = " "
    
    if request.method == "POST":

        Email_data = Email_Form(request.POST or None)
        if Email_data.is_valid():
           username = Email_data.cleaned_data['sendmail']
           print(username)
    else:
        Email_data = Email_Form()

    context = {
        'usename' : username
    }

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html', {})

def blog_list(request):
    return render(request, 'blog-list.html', {})

def U_brain(request):
    return render(request, 'U_brain.html', {})

def It_companies(request):
    return render(request, 'It_companies.html', {})

def javascript_framework(request):
    return render(request, 'javascript_framework.html')