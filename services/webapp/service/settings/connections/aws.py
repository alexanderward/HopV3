import os

import boto3


class AWS:
    @staticmethod
    def client(service, region_name, localstack=True, **kwargs):
        if not localstack:
            return boto3.client(service, region_name=region_name)
        session = boto3.session.Session()
        endpoint_url = kwargs.get('endpoint_url', os.environ["LOCALSTACK_FQDN"])
        return session.client(
            region_name=region_name,
            service_name=service,
            aws_access_key_id='aaa',
            aws_secret_access_key='bbb',
            endpoint_url=endpoint_url,
        )
