from django.conf.urls import url
from . import views

app_name = "myapp"

urlpatterns = [
    url(r'^templates/', views.index_template, name='index_template'),
]
