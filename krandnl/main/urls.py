from django.urls import path
from .views import home, about_app
from django.views.generic import TemplateView

urlpatterns = [
    path('', home, name='home'),
    path('aboutapp/', about_app, name='about_app'),
    path('history/', TemplateView.as_view(template_name='main/history.html'), name='history'),
    path('variations/', TemplateView.as_view(template_name='main/variations.html'), name='variations'),
    path('about/', TemplateView.as_view(template_name='main/about.html'), name='about'),
] 