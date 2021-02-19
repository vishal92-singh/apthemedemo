from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('about/', views.about, name='about'),
    path('agent_single/', views.agent_single, name='agent_single'),
    path('agents_grid/', views.agents_grid, name='agents_grid'),
    path('blog_grid/', views.blog_grid, name='blog_grid'),
    path('blog_single/', views.blog_single, name='blog_single'),
    path('contact/', views.contact, name='contact'),
    path('property_grid/', views.property_grid, name='property_grid'),
    path('property_single/', views.property_single, name='property_single'),


]