from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import View
from django.conf import settings
from django.utils.decorators import decorator_from_middleware
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from http.client import HTTPConnection

from influxproxy_base.misc import collectd_to_influxdb
from influxproxy_base.middleware import ProxyBasicAuthMiddleware


class BaseProxy (View):


    @method_decorator(csrf_exempt)
    @method_decorator(
        decorator_from_middleware(ProxyBasicAuthMiddleware))
    def dispatch(self, *args, **kwargs):
        return super(BaseProxy, self).dispatch(*args, **kwargs)

    def post(self, request):

        data = str(request.body)

        if not data:
            return HttpResponse(content="no data received", status=500)

        headers = {'Content-type': 'application/json'}
        influx_data = collectd_to_influxdb(request.read().decode('utf-8'),
                                           request.influxproxy_client.prefix)
        conn = HTTPConnection('%s:%s' %
                              (settings.INFLUX_HOST, settings.INFLUX_PORT))
        conn.request('POST', '/db/%s/series?u=%s&p=%s&time_precision=s' %
                     (request.influxproxy_client.client.influx_database,
                      settings.INFLUX_USER, settings.INFLUX_PASSWORD),
                     body=influx_data, headers=headers)
        r = conn.getresponse()

        if r.status == 200:
            return HttpResponse(content=r.read(), status=200)
        else:
            return HttpResponse(content='%s %s' % (r.status, r.read()), status=500)

