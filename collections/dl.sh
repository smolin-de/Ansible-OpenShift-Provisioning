#!/usr/bin/env bash

ansible-galaxy collection download ansible.posix -p .
ansible-galaxy collection download community.crypto -p .
ansible-galaxy collection download community.general -p .
ansible-galaxy collection download community.kubernetes -p .
ansible-galaxy collection download community.libvirt -p .

ansible-galaxy collection download ibm.ibm_zhmc -p .


