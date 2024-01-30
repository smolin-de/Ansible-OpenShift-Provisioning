.DEFAULT_GOAL := help

SHELL = /bin/bash -o pipefail

ALL_YAML_FILE = inventories/default/group_vars/all.yaml
HOST_FILE = inventories/default/hosts
OCP_CREDS_YAML_FILE = /tmp/ocp-secret.yaml

help:
	@echo "usage: make setup cluster=<cluster name>"
	@echo
	@echo "  e.g. make setup cluster=ocp2"

clean:
	@echo "Delete temp files..."
	@rm -f $(OCP_CREDS_YAML_FILE)
	@echo "Reset ansible host file..."
	@echo "[localhost]" > $(HOST_FILE)
	@echo "127.0.0.1 ansible_connection=local" >> $(HOST_FILE)

get-secret:
	@echo "Get required credentials..."
	@./get-sm-secret.py "multiarch.aop-secret-$(cluster).yaml" | base64 -d 1> $(OCP_CREDS_YAML_FILE)

test:
	@cat ./test.yaml | grep "^    version:"
ifdef ocp-version
	gsed -i "    version: .*/    version: 123/g" ./test.yaml
#	sed "^    version: .*/    version: $(ocp-version)/g" ./test.yaml
endif
	@cat ./test.yaml | grep "^    version:"

setup: clean get-secret
ifndef cluster
	$(error 'cluster' is undefined)
endif
# Create all.yaml file with credentials
	@echo "Create all.yaml file..."
	@jinja2 "clusters/$(cluster)-cluster.j2" $(OCP_CREDS_YAML_FILE) -o $(ALL_YAML_FILE)
# Run AOP setup
	ansible-playbook playbooks/0_setup.yaml

.PHONY: help clean get-secret test setup
