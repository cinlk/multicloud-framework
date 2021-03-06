# Copyright (c) 2017 Wind River Systems, Inc.
# Copyright (c) 2017-2018 VMware, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

import os

# [MSB]
MSB_SERVICE_IP = '127.0.0.1'
MSB_SERVICE_PORT = '10080'


# [ESR]
# ESR_GET_VIM_URI = "/api/extsys/v1/vims"

# [A&AI]
AAI_ADDR = "aai.api.simpledemo.openecomp.org"
AAI_PORT = "8443"
AAI_SERVICE_URL = 'https://%s:%s/aai' % (AAI_ADDR, AAI_PORT)
AAI_SCHEMA_VERSION = "v11"
AAI_USERNAME = 'AAI'
AAI_PASSWORD = 'AAI'

# [IMAGE LOCAL PATH]
ROOT_PATH = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# [register]
REG_TO_MSB_WHEN_START = False
REG_TO_MSB_REG_URL = "/api/microservices/v1/services"
REG_TO_MSB_REG_PARAM = {
    "serviceName": "multicloud",
    "version": "v0",
    "url": "/api/multicloud/v0",
    "protocol": "REST",
    "visualRange": "1",
    "nodes": [{
        "ip": "127.0.0.1",
        "port": "9001",
        "ttl": 0
    }]
}
