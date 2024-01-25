from django.shortcuts import render

# Create your views here.

def index(request):
      return render(request,'web/index.html')

def error(request):
      return render(request,'web/404.html')

def about(request):
      return render(request,'web/about.html')

def account_dashboard(request):
      return render(request,'web/account_dashboard.html')

def account_edit_address(request):
      return render(request,'web/account_edit_address.html')

def account_edit(request):
      return render(request,'web/account_edit.html')