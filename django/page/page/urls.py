from django.urls import path
from django.conf.urls import url
from . mport view
urlpatterns = [
    url(r'^$',view.hello),
]
