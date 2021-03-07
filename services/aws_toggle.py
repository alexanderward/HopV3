import boto3


class AWS:
    @staticmethod
    def client(service, localstack=True, **kwargs):
        if not localstack:
            return boto3.client(service, region_name=kwargs.get('region_name', 'us-east-1'))
        session = boto3.session.Session()
        endpoint_url = kwargs.get('endpoint_url', "http://localhost:4566")
        return session.client(
            service_name=service,
            aws_access_key_id='aaa',
            aws_secret_access_key='bbb',
            endpoint_url=endpoint_url,
        )
