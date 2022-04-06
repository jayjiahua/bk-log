# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making BK-LOG 蓝鲸日志平台 available.
Copyright (C) 2021 THL A29 Limited, a Tencent company.  All rights reserved.
BK-LOG 蓝鲸日志平台 is licensed under the MIT License.
License for BK-LOG 蓝鲸日志平台:
--------------------------------------------------------------------
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
We undertake not to change the open source license (MIT license) applicable to the current version of
the project delivered to anyone in the future.
"""
import os

from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from blueapps.account.decorators import login_exempt

# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt
from apps.utils.db import get_toggle_data


class HttpResponseIndexRedirect(HttpResponseRedirect):
    def __init__(self, redirect_to, *args, **kwargs):
        super(HttpResponseIndexRedirect, self).__init__(redirect_to, *args, **kwargs)
        self["Location"] = os.path.join(settings.DEFAULT_HTTPS_HOST, redirect_to.lstrip("/"))


def home(request):
    """
    首页
    """
    if not request.is_secure() and settings.DEFAULT_HTTPS_HOST:
        return HttpResponseIndexRedirect(request.path)
    return render(request, settings.VUE_INDEX, get_toggle_data())


def bkdata_auth(request):
    """
    鉴权页面
    """
    return render(request, "auth.html")


@login_exempt
def contact(request):
    """
    联系我们
    """
    return JsonResponse({"data": "login_exempt"})


@login_exempt
def healthz(request):
    return JsonResponse({"server_up": 1})


@login_exempt
def metrics(request):
    from django_prometheus import exports

    return exports.ExportToDjangoView(request)
