#!/usr/bin/env python
"""
    Created by howie.hu at 2021/4/10.
    Description：
    Changelog: all notable changes to this file will be documented
"""

import os

HOST = os.getenv("CC_HOST", "127.0.0.1")
HTTP_PORT = os.getenv("CC_HTTP_PORT", 8060)
WORKERS = os.getenv("CC_WORKERS", 1)
MAX_REQUEST = int(os.getenv("MAX_REQUEST", 10000))


bind = f"{HOST}:{HTTP_PORT}"
worker_class = "gevent"
workers = WORKERS
graceful_timeout = 30
max_requests = MAX_REQUEST
preload = True
