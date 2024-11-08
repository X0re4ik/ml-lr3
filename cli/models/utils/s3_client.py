import boto3
import botocore
import botocore.client  


def get_boto3_client(
    s3_access_key_id: str,
    s3_secret_access_key: str,
    s3_endpoint_url: str,
) -> botocore.client.S3ControlArnParamHandler:
    return boto3.client(
        "s3",
        endpoint_url=s3_endpoint_url,
        aws_access_key_id=s3_access_key_id,
        aws_secret_access_key=s3_secret_access_key,
    )
