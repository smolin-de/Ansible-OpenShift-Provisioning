#!/usr/bin/env python3

import json
import os
import sys

from ibm_cloud_sdk_core.authenticators.iam_authenticator import IAMAuthenticator
from ibm_secrets_manager_sdk.secrets_manager_v2 import *
from ibm_cloud_sdk_core.api_exception import ApiException

PROG_NAME = os.path.basename(sys.argv[0])
API_KEY = os.environ.get('IBMCLOUD_API_KEY', '')
# Secrets-Manager instance ID
INSTANCE_ID = 'dc1157e6-0b43-48b3-9384-025a8d26e12f'


def usage():
    """
    Display usage information for the script.
    """
    print(f"Usage: {PROG_NAME} <secret name>\n")
    print(f"  e.g. {PROG_NAME} multiarch.aop-secret-ocp3.yaml [SM-INSTANCE-ID]")


def get_secret(secret_name):
    """
    Retrieve and print the secret content from IBM Secrets Manager.

    :param secret_name: The name of the secret to retrieve.
    """
    try:
        secrets_manager_service = SecretsManagerV2(
            authenticator=IAMAuthenticator(apikey=API_KEY))

        secrets_manager_service.set_service_url(
            f'https://{INSTANCE_ID}.eu-de.secrets-manager.appdomain.cloud')

        all_results = []
        pager = SecretsPager(
            client=secrets_manager_service,
            sort='created_at',
            search='arbitrary',
            )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        for item in all_results:
            if item['name'] == secret_name:
                response = secrets_manager_service.get_secret(id=item['id'])
                secret = response.get_result()
                print(json.dumps(secret['payload'], indent=4)[1:-1])
                return

        # Secret was not found
        print(f'ERROR: Credential \'{secret_name}\' not found !', file=sys.stderr)
        sys.exit(1)
    except ApiException as ex:
        print(f"ERROR: Invalid API key. {ex}", file=sys.stderr)
        sys.exit(1)


def main(argv):
    """
    Main function to execute the script.

    :param argv: Command line arguments.
    """
    global INSTANCE_ID

    if len(argv) == 1:
        usage()
        sys.exit(1)
    if API_KEY == '':
        print("ERROR: 'IBMCLOUD_API_KEY' is not defined", file=sys.stderr)
        sys.exit(1)
    if len(argv) == 3:
        INSTANCE_ID = argv[2]
    get_secret(argv[1])


if __name__ == "__main__":
    main(sys.argv)
