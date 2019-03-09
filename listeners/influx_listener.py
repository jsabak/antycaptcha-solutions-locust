### reporting
from time import time
from locust import events
from logging import getLogger
from influxdb import InfluxDBClient

log = getLogger(__name__)

DATABASE_NAME = 'test_details'

client = InfluxDBClient('localhost', 8086, 'root', 'root', DATABASE_NAME)  # TODO change plase of the configuration


def save_success(request_type, name, response_time, response_length, **kw):
    json_body = [
        {
            'measurement': name,
            'tags': {
                'request_type': request_type,
                'success': "SUCCESS"
            },
            'time': int(time() * 1000000),
            'fields': {
                'response_time': response_time,
                'response_length': response_length
            }
        }
    ]
    # print(json_body)
    client.write_points(json_body)


def save_failure(request_type, name, response_time, response_length, **kw):
    json_body = [
        {
            'measurement': name,
            'tags': {
                'request_type': request_type,
                'success': "FAILURE"
            },
            'time': int(time() * 1000000),
            'fields': {
                "response_time": int(response_time),
                "response_length": int(response_length)
            }
        }
    ]
    client.write_points(json_body)


events.request_success += save_success
events.request_failure += save_failure
