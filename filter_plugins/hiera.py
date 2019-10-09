from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os
from ansible.utils.cmd_functions import run_cmd

def hiera(key):
    ANSIBLE_HIERA_CFG = os.getenv('ANSIBLE_HIERA_CFG', 'config/hiera.yaml')
    ANSIBLE_HIERA_BIN = os.getenv('ANSIBLE_HIERA_BIN', 'hiera')
    ANSIBLE_HIERA_FILTER = os.getenv('ANSIBLE_HIERA_FILTER', '/tmp/hiera_filter.json')

    rc, output, err = run_cmd("{0} -d -c {1} -j {2} {3}".format(
            ANSIBLE_HIERA_BIN, ANSIBLE_HIERA_CFG,ANSIBLE_HIERA_FILTER, key))

    return str(output.strip(),'utf-8')


class FilterModule(object):
    ''' Ansible core jinja2 filters '''

    def filters(self):
        return {
            # jinja2 overrides
            'hiera': hiera
            }
