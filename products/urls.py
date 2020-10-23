from django.conf.urls import url, include
from . import views
from django.urls import path


urlpatterns = [
    url(r'^detail/(?P<product_id>\w+)$', views.detail, name='detail')
]
