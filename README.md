influxproxy
===========

General
-------

Influxproxy is Python/Django based app that acts as proxy between **collectd write_http** and **influxdb**. It supports multiple influx databases backends. Decision about to which database data should be send is based on http simple auth and interal user system. Idea of application is based on https://github.com/bpaquet/collectd-influxdb-proxy.

Dependencies
------------

### Application

* Python 3.x
* Django 1.9.x

### Runtime

* InfluxDB 0.8.x


Configuration
-------------


Deployment of application does not differ from running any other Django app. You need to have working influxdb infrastructure. First you need to make changes to settings.py and set:

* SQL database backend (for internal application purposes), 
* Influxdb backend 

Configure collectd write_http plugin as follows:

    LoadPlugin "write_http"
    <Plugin "write_http">
      <URL "http://<influxproxy_ip>:<influxproxy_port>/data/">
        Format "JSON"
        User "INFLUX_PROXY_USER"
        Password "INFLUX_PROXY_PASSWORD"
      </URL>
    </Plugin>


You can access admin interface via: http://<influxproxy_ip>:<influxproxy_port>/admin/ where you could define influxproxyusers.

