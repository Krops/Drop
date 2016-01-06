from django.conf.urls import url
from blog.views import homeview

urlpatterns = [
    url(r'^$', homeview.as_view(), name='index'),
]
