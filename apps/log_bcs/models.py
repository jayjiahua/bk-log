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
"""
from django.db import models

from apps.models import SoftDeleteModel
from django.utils.translation import ugettext_lazy as _


class BcsClusterInfo(SoftDeleteModel):
    cluster_id = models.CharField(_("集群ID"), max_length=128, primary_key=True)
    bk_biz_id = models.IntegerField(_("业务ID"))
    project_id = models.CharField(_("项目ID"), max_length=128)
    is_active = models.BooleanField(_("是否开启日志采集"), default=True)

    @classmethod
    def active_bcs_cluster(cls, cluster_id, bk_biz_id, project_id):
        qs = cls.objects.filter(cluster_id=cluster_id)
        if qs.exists():
            qs.update(is_active=True)
            return
        cls.objects.create(cluster_id=cluster_id, bk_biz_id=bk_biz_id, project_id=project_id)

    @classmethod
    def stop_bcs_cluster(cls, cluster_id):
        qs = cls.objects.filter(cluster_id=cluster_id)
        if not qs.exists():
            return
        qs.update(is_active=False)
