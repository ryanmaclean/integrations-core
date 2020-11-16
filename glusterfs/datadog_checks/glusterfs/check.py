# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import json
from typing import Any

from datadog_checks.base import AgentCheck
from datadog_checks.base.utils.subprocess_output import get_subprocess_output

CLUSTER_STATS = {
    'node_count': 'cluster.node.count',
    'nodes_active': 'cluster.nodes.active',
    'volumes_started': 'volumes.started',
    'volume_count': 'volumes.count'
}

VOLUME_STATS = {

}

GLUSTER_VERSION = 'glfs_version'
CLUSTER_STATUS = 'cluster_status'

class GlusterfsCheck(AgentCheck):
    __NAMESPACE__ = 'glusterfs'

    def check(self, _):
        # type: (Any) -> None
        self._tags = self.instance.get('tags', [])
        output, _, _ = get_subprocess_output(['gstatus', '-a', '-o', 'json'], self.log)
        gstatus = json.loads(output)
        if 'data' in gstatus:
            data = gstatus['data']
            for key, metric in CLUSTER_STATS.items():
                if key in data:
                    self.gauge(metric, data[key], self._tags)
            self.parse_volume_summary(data)
        else:
            self.log.warning("No data from gstatus")

    def parse_volume_summary(self, output):
        if 'volume_summary' in output:
            volume_summary = output['volume_summary']

