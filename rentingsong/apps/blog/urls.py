# _*_ coding: utf-8 _*_
__author__ = 'rentingsong'
__date__ = '2020/8/8 12:33'

from django.conf.urls import url
from .views import BlogIndexView

urlpatterns = [
    url(r'^blog_index/$', BlogIndexView.as_view(), name="blog_index"),
]
