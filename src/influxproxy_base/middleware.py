from django.http import HttpResponse
from influxproxy_base.models import Client, ClientUser

import base64

class ProxyBasicAuthMiddleware(object):


    FAILSTRING = """"""

    def unauthed(self):

        response = HttpResponse(content=ProxyBasicAuthMiddleware.FAILSTRING,
                                content_type="text/html", status=401)
        response['WWW-Authenticate'] = 'Basic realm="Development"'
        return response

    def process_request(self, request):

        if not request.META.get('HTTP_AUTHORIZATION', None):
            return self.unauthed()

        else:
            authentication = request.META['HTTP_AUTHORIZATION']
            (method, auth) = authentication.split(' ', 1)

            if 'basic' != method.lower():
                return self.unauthed()

            auth = base64.b64decode(auth.strip()).decode('ascii')
            username, password = auth.split(':', 1)

            try:
                cu = ClientUser.objects.get(name=username)
            except ClientUser.DoesNotExist:
                return self.unauthed()

            if cu.password == password:
                request.influxproxy_client = cu
                return None

            return self.unauthed()