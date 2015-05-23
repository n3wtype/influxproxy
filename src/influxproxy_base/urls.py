from django.conf.urls import url

from influxproxy_base.views import BaseProxy


urlpatterns = [
    url(r'^', BaseProxy.as_view()),

]