#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from muchos.config.base import BaseConfig, SERVICES, OPTIONAL_SERVICES, HOST_VAR_DEFAULTS, PLAY_VAR_DEFAULTS, host_var, play_var, required, default
from muchos.config.existing import ExistingDeployConfig
from muchos.config.ec2 import Ec2DeployConfig
from muchos.config.azure import AzureDeployConfig, AZURE_VAR_DEFAULTS 

from configparser import ConfigParser

def DeployConfig(deploy_path, config_path, hosts_path, checksums_path, templates_path, cluster_name):
    c = ConfigParser()
    c.read(config_path)
    cluster_type = c.get('general', 'cluster_type')

    if cluster_type == 'existing':
        return ExistingDeployConfig(deploy_path, config_path, hosts_path, checksums_path, templates_path, cluster_name)

    if cluster_type == 'ec2':
        return Ec2DeployConfig(deploy_path, config_path, hosts_path, checksums_path, templates_path, cluster_name)

    if cluster_type == 'azure':
        return AzureDeployConfig(deploy_path, config_path, hosts_path, checksums_path, templates_path, cluster_name)