from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'index'),
    path('team', views.team, name = 'team'),
    path('services', views.services, name = 'services'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('blog', views.blog, name = 'blog'),
    path('single/<int:id>', views.singleblog, name = 'single')
]
