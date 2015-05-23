import json


def collectd_to_influxdb(str_data, prefix):

    data = json.loads(str_data)
    ret_data = []

    for v in data:
        for i in range(0, len(v['values'])):

            tmp_data = {'columns': ['time', 'value']}

            name = ''
            if len(prefix) > 0:
                name += '%s.' % prefix
            name += '%s.' % v['host']
            name += '%s.' % v['plugin']

            if len(v['plugin_instance']) > 0:
                name += '%s.' % v['plugin_instance']

            name += '%s.' % v['type']

            if len(v['type_instance']) > 0:
                name += '%s.' % v['type_instance']

            name += '%s' % v['dsnames'][i]

            tmp_data['name'] = name
            tmp_data['points'] = [[v['time'], v['values'][i]]]

            ret_data.append(tmp_data)

    return json.dumps(ret_data)

