from django.shortcuts import render
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
   path('', views.home, name='home'),  # Home page
    path('services/',views.services,name='services'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact_view, name='contact'),
    path('privacy/',views.privacy,name='privacy'),
    path('terms/',views.terms,name='terms'),
    path('contact-success/', TemplateView.as_view(template_name='contact_success.html'), name='contact_success'), 
   
     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
