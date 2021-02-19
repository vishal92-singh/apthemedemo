from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render(request, 'front/index.html')
def about(request):
    return render(request, 'front/about.html')
def agent_single(request):
    return render(request, 'front/agent-single.html')
def agents_grid(request):
    return render(request, 'front/agents-grid.html')
def blog_grid(request):
    return render(request, 'front/blog-grid.html')
def blog_single(request):
    return render(request, 'front/blog-single.html')
def contact(request):
    return render(request, 'front/contact.html')
def property_grid(request):
    return render(request, 'front/property-grid.html')
def property_single(request):
    return render(request, 'front/property-single.html')

