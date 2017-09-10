from django.contrib.auth.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage')
]
