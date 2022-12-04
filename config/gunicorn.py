""" Gunicorn 配置文件，更多说明：https://docs.gunicorn.org/en/latest/settings.html#settings
"""
import multiprocessing
import os
from distutils.util import strtobool

from . import Config, STATE

if STATE == 'dev':
    bind = f"0.0.0.0:{Config.WEB_PORT}"
    workers = int(os.getenv("WEB_CONCURRENCY", multiprocessing.cpu_count() * 2))
    worker_class = "gevent"
    # threads = int(os.getenv('PYTHON_MAX_THREADS', 1))

    # https://blog.csdn.net/pushiqiang/article/details/117197014
    # worker_tmp_dir = "/dev/shm"  # docker 中需要

    access_log_format = "%(h)s %(l)s %(u)s %(t)s '%(r)s' %(s)s %(b)s '%(f)s' '%(a)s' in %(D)sµs"  # noqa: E501
    """
        h           remote address
        l           '-'
        u           currently '-', may be user name in future releases
        t           date of the request
        r           status line (e.g. ``GET / HTTP/1.1``)
        s           status
        b           response length or '-'
        f           referer
        a           user agent
        T           request time in seconds
        D           request time in microseconds
        L           request time in decimal seconds
        p           process ID
        {Header}i   request header
        {Header}o   response header
    """
    reload = bool(strtobool(os.getenv("WEB_RELOAD", "false")))
else:
    # production
    bind = f"0.0.0.0:{Config.WEB_PORT}"

    workers = int(os.getenv("WEB_CONCURRENCY", multiprocessing.cpu_count() * 2))
    worker_class = "gevent"
    # threads = int(os.getenv('PYTHON_MAX_THREADS', 1))

    accesslog = "./log/gunicorn_access.log"
    access_log_format = "%(h)s %(l)s %(u)s %(t)s '%(r)s' %(s)s %(b)s '%(f)s' '%(a)s' in %(D)sµs"  # noqa: E501
    """
        h           remote address
        l           '-'
        u           currently '-', may be user name in future releases
        t           date of the request
        r           status line (e.g. ``GET / HTTP/1.1``)
        s           status
        b           response length or '-'
        f           referer
        a           user agent
        T           request time in seconds
        D           request time in microseconds
        L           request time in decimal seconds
        p           process ID
        {Header}i   request header
        {Header}o   response header
    """

    errorlog = "./log/gunicorn_error.log"
