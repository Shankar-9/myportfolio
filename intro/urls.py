from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.home, name='home'),
    path('journey.html', views.journey, name='journey'),
    path('aboutme.html', views.aboutme, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('projects.html',views.projects1, name='projects1'),
    path('skills.html', views.skills1, name='skills'),
    path('submit_form', views.submit, name='submit')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)