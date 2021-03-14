import os

import boto3


class AWS:
    @staticmethod
    def client(service, region_name, host, port, localstack=True):
        if not localstack:
            return boto3.client(service, region_name=region_name)
        session = boto3.session.Session()
        endpoint_url = f"http://{host}:{port}"
        return session.client(
            region_name=region_name,
            service_name=service,
            aws_access_key_id='aaa',
            aws_secret_access_key='bbb',
            endpoint_url=endpoint_url,
        )
