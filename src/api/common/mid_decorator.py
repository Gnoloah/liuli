"""
    Created by howie.hu at 2022-04-12.
    Description: 验证装饰器中间件
    Changelog: all notable changes to this file will be documented
"""


from functools import wraps

from flask import request
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request

from src.api.common.flask_tools import response_handle
from src.api.common.response_base import UniResponse


def jwt_required():
    """JWT校验装饰器"""

    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            if request.method == "POST":
                post_data: dict = request.json
                username = post_data.get("username")
                # 返回 401 就是验证错误
                verify_jwt_in_request()

                if get_jwt_identity() == username:
                    resp = fn(*args, **kwargs)
                else:
                    resp = response_handle(
                        request=request,
                        dict_value=UniResponse.NOT_AUTHORIZED,
                        status=401,
                    )
            else:
                resp = response_handle(
                    request=request,
                    dict_value=UniResponse.NOT_AUTHORIZED,
                    status=401,
                )
            return resp

        return decorator

    return wrapper
