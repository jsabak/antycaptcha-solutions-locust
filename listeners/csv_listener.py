### reporting
from time import time, strftime
from locust import events
from logging import getLogger

log = getLogger(__name__)

log_file_name = f'test_details_{strftime("%Y_%m_%d_%H_%M_%S")}.csv'

log_file = open(log_file_name, 'wt')
log_file.write('timestamp\tresult\tresponse_time\trequest_type\tname\tresponse_length\n')


def save_success(request_type, name, response_time, response_length, **kw):
    log_file.write(f'{int(time() * 1000)}\tSUCCESS\t{int(response_time)}\t{request_type}\t{name}\t{response_length}\n')
    log_file.flush()


def save_failure(request_type, name, response_time, response_length, **kw):
    log_file.write(f'{int(time() * 1000)}\tFAILURE\t{int(response_time)}\t{request_type}\t{name}\t{response_length}\n')
    log_file.flush()


def close_log_file(**kw):
    log_file.close()


events.request_success += save_success
events.request_failure += save_failure
events.quitting += close_log_file
