# ansible-hiera-filter-plugin

## Description

This is an ansible filter plugin for integration to Hiera

### Description

This plugin provides to reach confguration files with using Hiera. It might be usefull especially migration projects from puppet to ansible.


### Configuration

The plugin will look for the some environment variables as configuration of Hiera. If the variables are not set, it will use default values which set in filter_plugins/Hiera.py file.

`ANSIBLE_HIERA_CFG` : Hiera Hierarchie config file
`ANSIBLE_HIERA_BIN` : location of executable hiera
`ANSIBLE_HIERA_CFG` : hiera filter file


### Usage
First of all we need to set filter values to reach target env, account, e.g

```yaml
- name: set hiera filter
  shell: "echo '{ \"env\":\"{{ env_identifier }}\", \"account\":\"{{ acc_number }}\"  }' > /tmp/hiera_filter.json"
```

now we are ready to query variables via hiera filter inside ansible

```yaml
- name: get variable with using Hiera filter
  set_fact:
    env_name: "{{ 'variable_name' | Hiera }}"
```

### License

This project is licensed under the Apache 2.0 license, please the the LICENSE file included with this software.
