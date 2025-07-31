from test_app.views import home, contact, About
from django.urls import path

urlpatterns=[
    path('',home,name='home'),
    path('contact/',contact, name='contact'),
    path('about/', About, name='about'),
]